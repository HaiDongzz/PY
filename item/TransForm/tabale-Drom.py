import pandas as pd

# 读取CSV文件
data = pd.read_csv('D:\WPS\workspace\data.csv')

# 将数据保存为Excel文件
data.to_excel('S2-6~4.xlsx', index=False)
