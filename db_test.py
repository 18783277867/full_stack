import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Mysql20040101,",
    database="account_db",
    charset="utf8mb4"
)

print("数据库连接成功")

conn.close()
print("数据库连接已关闭")