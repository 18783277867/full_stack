'''
1. 连接 ws://localhost:8765
2. 持续接收服务端发来的 JSON
3. 解析 JSON
4. 自动插入 account_snapshot 表
'''
import asyncio
import json
import time

import pymysql
import websockets

from app.config import WS_URL
from app.db import get_connection
from app.repository import insert_account_snapshot


def connect_with_retry(max_retries=20, delay=3):
    for i in range(max_retries):
        try:
            conn = get_connection()
            print("MySQL 连接成功", flush=True)
            return conn
        except pymysql.MySQLError as e:
            print(f"MySQL 连接失败，第 {i + 1} 次重试：{e}", flush=True)
            time.sleep(delay)

    raise Exception("MySQL 多次重试后仍无法连接")


async def main():
    print(f"正在连接 {WS_URL} ...", flush=True)

    conn = connect_with_retry()

    try:
        async with websockets.connect(WS_URL) as websocket:
            print("WebSocket 连接成功，开始接收消息...\n", flush=True)

            while True:
                message = await websocket.recv()
                data = json.loads(message)

                print("收到消息:", data, flush=True)

                insert_account_snapshot(conn, data)
                print("已写入 MySQL", flush=True)
                print("-" * 50, flush=True)
    finally:
        conn.close()
        print("MySQL 连接已关闭", flush=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序已手动停止", flush=True)