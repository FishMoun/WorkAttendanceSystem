const { contextBridge, dialog,ipcRenderer } = require('electron');  

// 暴露给渲染进程的 API  
contextBridge.exposeInMainWorld('electronAPI', {  
  minimizeWindow: () => ipcRenderer.send('minimize-window'),  
  closeWindow: () => ipcRenderer.send('close-window')  ,
  openFile: () => ipcRenderer.invoke('open-dialog')
});