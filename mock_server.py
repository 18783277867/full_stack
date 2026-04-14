import asyncio
import json
import random
from datetime import datetime

import websockets


async def handler(websocket):
    print("客户端已连接")

    while True:
        data = {
            "account_id": "acc_001",
            "balance": round(random.uniform(10000, 20000), 2),
            "equity": round(random.uniform(10000, 20000), 2),
            "unrealized_pnl": round(random.uniform(-500, 500), 2),
            "currency": "USDT",
            "ts": datetime.now().isoformat()
        }

        await websocket.send(json.dumps(data, ensure_ascii=False))
        print("已发送:", data)

        await asyncio.sleep(3)


async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    print("WebSocket 服务已启动: ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())