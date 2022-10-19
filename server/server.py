#!/usr/bin/env python3

import asyncio
from websockets import serve
from pprint import pprint
import ssl
from pathlib import Path
from http import HTTPStatus

sockets = {}
PORT=8000

# Handles non-websockets requests
async def handle_http(path, request_headers):
    if "Upgrade" in request_headers:
        return

    response_headers = [
        ('Server', 'Ad-hoc server'),
        ('Connection', 'close'),
    ]

    if (path == "/websocket-speed-video-controller/" or path == "/websocket-speed-video-controller"):
        response_headers.append(('Content-Type', "text/html"))
        body = open("controller.html", 'rb').read()
        return HTTPStatus.OK, response_headers, body
    else:
        return HTTPStatus.NOT_FOUND, response_headers, b"404. But who are you and what are you doing here?"


# Handles a websocket connection during all its life
async def handle_websocket(websocket, path):
    global sockets

    sockets[websocket]=None

    # Bucle infinito asincrono
    async for message in websocket:
        #print("Message: ", message)
        if (message == "controller"):
            sockets[websocket] = "controller"
            print("New controller connected")
            pprint(sockets)
        elif (message == "player"):
            sockets[websocket] = "player"
            print("New player connected")
            pprint(sockets)
        else:
            for ws in list(sockets):
                if sockets[ws] == "player":
                    try:
                        await ws.send(message)
                    except Exception as e:
                        # Websocket was probably closed. Mark as unused
                        print("Excepcion" + str(e))
                        del sockets[ws]


async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
            Path(__file__).with_name('cert.crt'),
            keyfile=Path(__file__).with_name('cert.key')
    )

    async with serve(handle_websocket, "0.0.0.0", PORT, ssl=ssl_context, process_request=handle_http):
        await asyncio.Future()  # run forever

asyncio.run(main())
