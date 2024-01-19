<template>
  <el-container>
    <el-header class="my-header">
      <span class="title">考勤自动处理系统</span>
      <div class="header-button-area">
        <div class="header-button1" @click="minimizeWindow()">-</div>
        <div class="header-button2" @click="closeWindow()">x</div>
      </div>
    </el-header>
    <el-main class="my-main">
      <div class="select">
        <el-button type="primary" @click="selectFile()">选择考勤表</el-button>
        <el-input class="input" v-model="input" disabled placeholder="导入路径" />
      </div>
      <div class="analysis"></div>

      <el-button @click="startAnlysize()">开始分析</el-button>
      <el-button @click="exportResult()">导出结果</el-button>
      <div class="tip">{{ tip }}</div>
      <div class="info">made by fishmoun</div>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios'
import { ElMessage } from 'element-plus'
export default {
  data() {
    return {
      input: ''
      , tip: '请选择考勤表',
      exportpath:'',
      df:{},
      isSelected: false,
      isAnalysized: false
    }
  },
  methods: {
    //最小化窗口
    minimizeWindow() {
      window.electronAPI.minimizeWindow()
    },
    //关闭窗口
    closeWindow() {
      window.electronAPI.closeWindow()
    },
    //开始分析事件
    async startAnlysize() {
      if(this.isSelected){
      this.tip = '正在分析中...'
      axios({
        url:'http://127.0.0.1:5000/analysize',
        method:'post',
        data:{
          filepath: this.input
        }
      })
        .then( (response)=> {
          this.exportpath = response.data.filepath
          console.log(this.exportpath)
          this.tip = '已进行了分析'
        })
        .catch(function (error) {
          console.log(error);
        });
        }
      else 
        ElMessage.error('还没有选择文件!')
    },


    //导出结果事件
    // async exportResult() {
    //   axios({
    //     url: `http://127.0.0.1:5000/download/results.xlsx`, // 
    //     method: 'GET',
    //     responseType: 'blob', // 表明返回服务器响应的数据类型  
    //   }).then((response) => {
    //     const url = window.URL.createObjectURL(new Blob([response.data]));
    //     const link = document.createElement('a');
    //     link.href = url;
    //     link.setAttribute('download', 'results.xlsx'); // 设置下载的文件名  
    //     document.body.appendChild(link);
    //     link.click();
    //     document.body.removeChild(link);
    //   });
    // },
    exportResult(){
      // axios({
      //   url:'http://127.0.0.1:5000/export',
      //   method:'post',
      //   data:{
      //     df:this.df
      //   }
      // }).then((res)=>{
      //   console.log(res)
      //   this.exportpath = res.filepath
      // })
      if(this.isSelected)
      {
        if(this.exportpath)
            this.tip = this.exportpath

        else
          ElMessage.error('还没有开始分析！')
          }
      else
          ElMessage.error('还没有选择文件!')
        
    },
    checkFile(file) {
      console.log(file)
    },
    //选择文件系统的文件并获取文件信息
    async selectFile() {
      const filePath = await window.electronAPI.openFile();
      if (filePath) {
        this.input = filePath
        this.isSelected = true
        this.tip = '已选中文件'
      } else {
        ElMessage.error('选择失败！')
      }
    }
    // handleSuccess(response) {
    //   ElMessage.success('上传成功！')
    //   this.input = response.file_path
    // },
    // handleError(err) {
    //   ElMessage.error('上传失败,请重新上传')

    // }
  }
}


</script>

<style scoped>
.my-header {
  padding: 0;
  border-bottom: 1px solid #ccc;
  position: relative;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #E8E8E8;
  -webkit-app-region: drag;
}

.my-main {
  padding: 0;

}

.title {
  color: #000;
  font-weight: bold;
}

.header-button-area {
  position: absolute;
  display: flex;
  top: 0;
  right: 0;
  border: 0;
}

.header-button1 {
  height: 100%;
  background: #E8E8E8;
  border-bottom: 1px solid #ccc;
  width: 30px;
  -webkit-app-region: no-drag;
}

.header-button1:hover {
  color: #ccc;
  border: 0;
  cursor: pointer;
}

.header-button2 {
  height: 100%;
  background: #E8E8E8;
  width: 30px;
  -webkit-app-region: no-drag;
}

.header-button2:hover {
  color: red;
  border: 0;
  cursor: pointer;
}

.select {
  margin: 20px;
  display: flex;
}

.input {
  margin-left: 10px;
}

.tip {
  margin: 20px;
}

.info {
  position: absolute;
  bottom: 0;
  right: 5px;
  color: #c8c9cc;

}
</style>
