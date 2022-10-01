#!/usr/bin/env python3

import asyncio
from websockets import serve
from pprint import pprint
import ssl
from pathlib import Path

sockets = {}
PORT=8000

# La parte externa de la funcion solo se invoca 1 vez por websocket
async def echo(websocket, something):
    global sockets

    sockets[websocket]=None

    # Bucle infinito asincrono
    async for message in websocket:
        if (message == "controller"):
            sockets[websocket] = "controller"
            print("New controller connected")
            pprint(sockets)
        elif (message == "player"):
            sockets[websocket] = "player"
            print("New player connected")
            pprint(sockets)
        #print("Message: ", message)
        for ws in sockets:
            if sockets[ws] == "player":
                try:
                    await ws.send(message)
                except:
                    # Websocket was probably closed. Mark as unused
                    print("Excepcion")
                    sockets[ws]=None


async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
            Path(__file__).with_name('cert.crt'),
            keyfile=Path(__file__).with_name('cert.key')
    )

    async with serve(echo, "0.0.0.0", PORT, ssl=ssl_context):
        await asyncio.Future()  # run forever

asyncio.run(main())
