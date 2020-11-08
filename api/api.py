import json
import random

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


with open("./responses", "r") as resp:
    lines = [line.replace("\n", "") for line in resp.readlines()]


async def handle(request: Request) -> Response:
    ret = {
        "message": random.choice(lines),
    }
    return web.Response(text=json.dumps(ret))


app = web.Application()
app.router.add_get("/eightball", handle)

web.run_app(app)
