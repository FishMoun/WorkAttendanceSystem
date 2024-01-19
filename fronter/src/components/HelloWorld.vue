<template>
  <el-card>
    <el-upload action="http://127.0.0.1:5000/upload" :show-file-list="false" :on-success="handleSuccess">
      <el-button type="primary">选择考勤表</el-button>
    </el-upload>
    <el-input v-model="input" disabled placeholder="导入路径" />
    <el-button @click="startAnlysize()">开始分析</el-button>
    <el-button @click="exportResult()">导出结果</el-button>
  </el-card>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      input: ''
    }
  },
  methods: {
    //开始分析事件
    async startAnlysize() {
      axios.post('http://127.0.0.1:5000/analysize', {
        filepath: this.input
      })
        .then(function (response) {
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },


    //导出结果事件
    async exportResult() {
      axios({  
        url: `http://127.0.0.1:5000/download/results.xlsx`, // 
        method: 'GET',  
        responseType: 'blob', // 表明返回服务器响应的数据类型  
      }).then((response) => {  
        const url = window.URL.createObjectURL(new Blob([response.data]));  
        const link = document.createElement('a');  
        link.href = url;  
        link.setAttribute('download', 'results.xlsx'); // 设置下载的文件名  
        document.body.appendChild(link);  
        link.click();  
        document.body.removeChild(link);  
      });  
    },

    handleSuccess(response) {
      console.log(response)
      this.input = response.file_path
    }

  }
}


</script>

<style></style>
