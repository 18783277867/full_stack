import pymysql
from datetime import datetime

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Mysql20040101,",
    database="account_db",
    charset="utf8mb4"
)

sql = """
INSERT INTO account_snapshot
(account_id, balance, equity, unrealized_pnl, currency, ts)
VALUES (%s, %s, %s, %s, %s, %s)
"""

data = (
    "acc_001",
    10000.50,
    10200.80,
    200.30,
    "USDT",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

with conn.cursor() as cursor:
    cursor.execute(sql, data)

conn.commit()
print("插入成功")

conn.close()