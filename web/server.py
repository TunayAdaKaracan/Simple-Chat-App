import asyncio
import websockets
import json

connectClients = {}

async def handleClient(websocket):
    nick = await websocket.recv()
    connectClients[websocket] = nick
    print("New Client:", nick)

    await sendToClients({"type": "joinEvent", "name": nick})
    while True:
        try:
            msg = await websocket.recv()
        except:
            connectClients.pop(websocket)
            await sendToClients({"type": "quitEvent", "name": nick})
            return
        await sendToClients({"type": "messageEvent", "name": nick, "message": msg})


async def sendToClients(packet):
    for websocket in connectClients:
        await websocket.send(json.dumps(packet))


async def run():
    async with websockets.serve(handleClient, "", 8080):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(run())
