import json
import os
import random

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

with open("./api/responses", "r") as resp:
    lines = [line.replace("\n", "") for line in resp.readlines()]


async def index(request: Request) -> Response:
    return web.Response(text="Eightball response API - Marwynn Somridhivej")


async def handle(request: Request) -> Response:
    ret = {
        "message": random.choice(lines),
    }
    return web.Response(text=json.dumps(ret))


async def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_get("/eightball", handle)
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    web.run_app(create_app(), port=port)
