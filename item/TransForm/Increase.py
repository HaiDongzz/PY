import pandas as pd
from sqlalchemy import create_engine

# 读取Excel数据
excel_file = 'D:\Document-Data\DATA2.xlsx'
df = pd.read_excel(excel_file)

# 连接数据库  db_url = "oracle+cx_oracle://username:password@hostname:port_number/service_name"
engine = create_engine('oracle+cx_oracle://t_psmdb:Wzmtr@123456@10.11.76.40:1521/gisdb')

# 查询数据库表中已存在的名称
existing_names = pd.read_sql_query('SELECT * FROM T_PSMDB.T_BUS_SITE_MY', engine)

# with engine.connect() as connection:
#     result = connection.execute('select * from T_PSMDB.T_BUS_SITE_MY')
#     for row in result:
#         print(row)


# 筛选出不重复的数据
unique_data = df[~df['SITE_NAME'].isin(existing_names['SITE_NAME'])]

# 插入唯一数据到数据库表
table_name = 'T_PSMDB.T_BUS_SITE_MY'
unique_data.to_sql(table_name, engine, if_exists='append', index=False)
