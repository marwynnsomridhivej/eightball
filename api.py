import json
import os
import random

from aiohttp import web
from aiohttp.web import Request, Response

with open("./responses", "r") as resp:
    lines = [line.replace("\n", "") for line in resp.readlines()]


async def index(request: Request) -> Response:
    return web.Response(text="Eightball response API - Marwynn Somridhivej")


async def handle(request: Request) -> Response:
    ret = {
        "question": request.query.get("question", "None"),
        "message": random.choice(lines),
    }
    return web.json_response(ret)


async def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_get("/eightball", handle)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=int(os.environ.get("PORT", 8080)))
