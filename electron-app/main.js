// main.js  
  
// 引入 Electron 模块  
const { app, BrowserWindow ,ipcMain,dialog } = require('electron');  
const path = require('node:path')
// 保持对应用程序窗口的引用  
let mainWindow;  
  
// 创建应用程序窗口的函数  
function createWindow() {  
  // 创建浏览器窗口  
  mainWindow = new BrowserWindow({  
    width: 500,  
    height: 250,  
    resizable: false ,
    titleBarStyle: 'hidden' ,
    
    webPreferences: {  
      preload: path.join(__dirname, 'preload.js'),
      // 在这里配置网页的偏好设置，比如 nodeIntegration  
      nodeIntegration: true,  
    },  
  });  
  
  // 加载 index.html 文件  
  //  mainWindow.loadFile('http://localhost:5173/');  
  mainWindow.loadFile('dist/index.html')
  // 打开开发者工具  
  // mainWindow.webContents.openDevTools();  
  
  // 当窗口被关闭时，释放对该窗口的引用  
  mainWindow.on('closed', function () {  
    mainWindow = null;  
  });  
}  
ipcMain.on('minimize-window', () => {  
  mainWindow.minimize();  
});  
  
ipcMain.on('close-window', () => {  
  mainWindow.close();  
});
ipcMain.handle('open-dialog',async () =>{
   
  const { canceled, filePaths } = await dialog.showOpenDialog({filters:[{name:'表格',extensions:['xls']}]})
  if (!canceled) {
    return filePaths[0]
  }
   
})

// Electron 会在初始化后并准备创建浏览器窗口时，调用这个函数  
app.whenReady().then(createWindow);  
  
// 当全部窗口关闭时退出应用  
app.on('window-all-closed', function () {  
  // 在 macOS 上，除非用户用 Cmd + Q 确定地退出，否则绝大部分应用及其菜单栏会保持激活  
  if (process.platform !== 'darwin') app.quit();  
});  
  
app.on('activate', function () {  
  // 在 macOS 上，当点击 dock 图标并且该应用中没有其他打开的窗口时，通常在应用中重新创建一个窗口  
  if (BrowserWindow.getAllWindows().length === 0) createWindow();  
});