import asyncio
import websockets
import time


async def fun(websocket, path):
    while True:
        await asyncio.sleep(1)
        reply = input("Server-->")
        await websocket.send(reply)
        print(f"message sent:{reply}")
        msg = await websocket.recv()
        print(f"Client-->{msg}")
        x = int(input("Press 1 for chat and Press 2 for keeping connection alive-"))
        if x == 2:
            while True:
                await asyncio.sleep(1)
                reply = "Connection Alive"
                await websocket.send(reply)
                print(f"message sent:{reply}")
                msg = await websocket.recv()
                print(msg)


start_server = websockets.serve(fun, 'localhost', 8769)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
