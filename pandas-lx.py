import numpy as nu
import pandas as pd
import xlwt
import xlrd
import os,sys

df=pd.read_excel(r'E:\python\money.xls',sheet_name="money")
# print(df.iloc[1].values)
# print(df.iloc[[0,1,2]].values)
# print(df.iloc[0,1])
# print(df.loc[:,['姓名']]) #读取制定表格下列名为“姓名"下的数据
# print(df.index.values) #读取行号

# 将修改后的数据写入表格“计算”
# dataframe=df.loc[:,['姓名']]
# dataframe.to_excel(r'E:\python\2.xls',index=False)
# os.startfile(r'E:\python\计算.xls')

# print(df.head())
# os.startfile(r'E:\python\money.xls')
print(df.columns)
s=df.columns(['交易类型'])
# print(df.columns[1])
