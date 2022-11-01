import asyncio
import websockets


async def sendback(websocket):
    with open("data", "r") as data:
        wall = data.read()
        await websocket.send(wall)
        print("A client connected.")
    name = await websocket.recv()
    with open("data", "a") as data:
        data.write("\n\n————————————————\n\n"+name)
        print("A client send something.")

start_server = websockets.serve(sendback, "0.0.0.0", 35888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()