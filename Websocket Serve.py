import asyncio
import websockets


async def hello():
    async with websockets.connect(
            'ws://localhost:8769') as websocket:
        while True:
            await asyncio.sleep(1)
            reply = await websocket.recv()
            if str(reply)=="Connection Alive":
                print(reply)
                await websocket.send("Yes")
                print("Yes")
            else:
                print(f"Server-->{reply}")
                msg = input("Client-->")
                await websocket.send(msg)
                print(f"message sent:{msg}")


asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
