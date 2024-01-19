import { createApp } from 'vue'
//element-ui引入
import ElementPlus from 'element-plus'  
import 'element-plus/dist/index.css' 
import './style.css'
import App from './App.vue'


//挂载App
const app = createApp(App)  
app.use(ElementPlus)  
app.mount('#app')