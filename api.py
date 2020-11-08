import json
import os
import random

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import route

with open("./api/responses", "r") as resp:
    lines = [line.replace("\n", "") for line in resp.readlines()]


@route.get("/")
async def index(request: Request) -> Response:
    return web.Response(text="Eightball response API - Marwynn Somridhivej")


@route.get("/eightball")
async def handle(request: Request) -> Response:
    ret = {
        "message": random.choice(lines),
    }
    return web.Response(text=json.dumps(ret))


async def create_app() -> web.Application:
    app = web.Application()
    app.add_routes(route)
    return app
