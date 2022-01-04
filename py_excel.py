import pandas as pd
import numpy as np

file ='D:\\Jupyter\\job.xlsx'
x = ['java','c++','PHP','Android','iOS','Python','web前端']
s= ['Sheet1','Sheet2','Sheet3','Sheet4','Sheet5','Sheet6','Sheet7']
for i in range(0,6):
    data = pd.read_excel(file,sheet_name=s[i]) #reading file
    java=data['平均工资'].values.tolist()
    jmean=np.mean(java)
    print(x[i],'工资平均值:',jmean)
