import asyncio
import os

from aiohttp import web
from cbpi.api import *


class MyActor(CBPiActor):

    def on(self, power):
        print("MY ACTOR ON AMAZING")

    def off(self):
        print("MY ACTOR OFF")


class MyActor2(CBPiActor):

    def on(self, power):
        print("MY ACTOR ON AMAZING")

    def off(self):
        print("MY ACTOR OFF")

class MyExt(CBPiExtension):

    def __init__(self, cbpi):
        '''
        Initializer

        :param cbpi:
        '''
        self.cbpi = cbpi
        # register component for http, events
        # In addtion the sub folder static is exposed to access static content via http
        path = os.path.dirname(__file__)

        self.cbpi.register(self, "/myext", static=os.path.join(path, "static"))

    @request_mapping(path="/", auth_required=False)
    def hello_world(self, request):
        return web.Response(text="Hello, world")

    @on_event(topic="actor/#")
    async def listen(self, **kwargs):
        print("MY EXT ........", kwargs)
        pass

def setup(cbpi):
    '''
    This method is called by the server during startup
    Here you need to register your plugins at the server

    :param cbpi: the cbpi core
    :return:
    '''


    cbpi.plugin.register("MyActor", MyActor)
    cbpi.plugin.register("MyActor", MyActor)
    cbpi.plugin.register("MyActor2", MyActor2)
    cbpi.plugin.register("MyExt", MyExt)
