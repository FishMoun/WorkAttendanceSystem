# =================================
# File : handle_excel.py
# Description : 
# Author : QinLing
# CREATE TIME : 2024/1/12 16:50
# =================================
import pandas as pd
from antlr4handler import time_handler
import re
from z3 import *
class HandleExcelFactory:


    def __init__(self, filepath):
        self.filepath = filepath

    def workattendace_process(self):
        sheet_name = '考勤记录'
        # 创建一个输出df,直接用示例中的数据表
        dfout = pd.read_excel(self.filepath, sheet_name='输出格式示例')

        # 获取df的列名
        dfout_columns = dfout.columns.tolist()

        # 读取Excel文件中的特定工作表
        df = pd.read_excel(self.filepath, sheet_name=sheet_name)
        # 操作原df的值赋值给新的df
        # 从第5个数据开始读取
        datalist = []
        for i in range(0, df.shape[0], 2):
            row1 = df.iloc[i]
            row2 = df.iloc[i + 1]
            # 处理好数据后，向列表中填充数据
            data = []
            data.append(row1['人员名称'])
            # 处理上班时间
            if (not isinstance(row1['打卡时间'],str)) or (not isinstance(row2['打卡时间'],str)):
                worktime = ''
            else:
                worktime = row1['打卡时间'] + '-' + row2['打卡时间']
            data.append(worktime)
            # 处理上班时长
            # 先利用antlr4解析时间，再计算，最后拼接
            if not worktime == '':
                time1 = time_handler.handler(row1['打卡时间'])
                time2 = time_handler.handler(row2['打卡时间'])
                data.append(self.calculate_timestr(time1[0], time1[1], time2[0], time2[1]))
            else:
                data.append('')
            #添加其他行
            data += row1.iloc[1:4].tolist()
            data += row1.iloc[4:15].tolist()
            data += row2.iloc[4:15].tolist()
            datalist.append(data)
            # outrow = pd.DataFrame([data], columns=dfout_columns)
            # dfout = dfout.append(outrow, ignore_index=True)
        dfout2 = pd.DataFrame(datalist, columns=dfout_columns)
        dfout2['上班时间达标情况'] = dfout2['上班时长'].apply(self.judge_worktime)
        # 输出新df
        # dfout2.to_excel("uploads/results.xlsx", index=False)
        return dfout2
    def calculate_timestr(self, h1, m1, h2, m2):
        h = h2 - h1
        m = m2 - m1
        if m < 0:
            m += 60
            h -= 1
        return str(h) + 'hours' + str(m) + 'mins'
    def judge_worktime(self,x):
        if x :
            match = re.search(r'\d+(?=hours)', x)
            if match:
                s = Solver()
                va = Int('va')
                s.add(va>8)

                s.add(va == int(match.group()))
                if s.check() == sat:
                    return '已达标'
                else:
                    return '未达标'


        else:
            return ''
