import asyncio
import websockets
import time


async def msg():
    async with websockets.connect('ws://localhost:8767') as websocket:
        while True:
            await asyncio.sleep(2)
            await websocket.send('test message')
            msg = await websocket.recv()
            print(msg)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(msg())
    asyncio.get_event_loop().run_forever()
