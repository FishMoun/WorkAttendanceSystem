import os

import pandas as pd
from flask import Flask, request, jsonify,send_from_directory,session
from flask_cors import CORS
from handle_excel import HandleExcelFactory

app = Flask(__name__)
CORS(app)


# 设置上传文件夹
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/', methods=['POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/upload', methods=['POST'])
def uploadExcelFile():
    print('123')
    print(request)
    file = request.files['file']

    # 如果用户没有选择文件，则浏览器会提交一个空文件
    if file.filename == '':
        return jsonify({'message': '没有选择文件'}), 400

        # 文件保存路径
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # 保存文件
    file.save(file_path)

    return jsonify({'message': '文件上传成功', 'file_path': file_path})


#对excel表格进行操作
@app.route('/analysize', methods=['POST'])
def analysizeFile():
    data = request.get_json()

    # 这里是对文件进行分析并导出文档
    # 1查找文档
    filepath = data.get('filepath')
    # 2分析文档 处理excel诗句
    excelhandler = HandleExcelFactory(filepath)
    df = excelhandler.workattendace_process()
    df.to_excel("results.xlsx", index=False)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return jsonify({'filepath': os.path.join(current_dir, "results.xlsx")})

@app.route('/download/<path:path>')
def download_file(path):
    return send_from_directory('uploads', path)

@app.route('/export',methods=['POST'])
def export_file():
    data = request.get_json()
    df = pd.DataFrame(data.df)
    if df :
        df.to_excel("results.xlsx", index=False)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return jsonify({'filepath':os.path.join(current_dir,"results.xlsx")})

if __name__ == '__main__':
    app.run()
