from cbpi_api import *


class MyActor(CBPiActor):

    def on(self, power):
        print("MY ACTOR ON AMAZING")

    def off(self):
        print("MY ACTOR OFF")


def setup(cbpi):
    '''
    This method is called by the server during startup
    Here you need to register your plugins at the server

    :param cbpi: the cbpi core
    :return:
    '''


    cbpi.plugin.register("MyActor", MyActor)