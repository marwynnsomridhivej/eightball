import json
import os
import random

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

with open("./api/responses", "r") as resp:
    lines = [line.replace("\n", "") for line in resp.readlines()]


async def handle(request: Request) -> Response:
    ret = {
        "message": random.choice(lines),
    }
    return web.Response(text=json.dumps(ret))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app = web.Application()
    app.add_routes([web.get("/eightball", handle)])
    web.run_app(app, port=port)
