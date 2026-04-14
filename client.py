'''
1. 连接 ws://localhost:8765
2. 持续接收服务端发来的 JSON
3. 解析 JSON
4. 自动插入 account_snapshot 表
'''
import asyncio
import json

import websockets

from app.config import WS_URL
from app.db import get_connection
from app.repository import insert_account_snapshot


async def main():
    print(f"正在连接 {WS_URL} ...")

    conn = get_connection()
    print("MySQL 连接成功")

    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket 连接成功，开始接收消息...\n")

        while True:
            message = await websocket.recv()
            data = json.loads(message)

            print("收到消息:", data)

            insert_account_snapshot(conn, data)
            print("已写入 MySQL")
            print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())