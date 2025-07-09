import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
import hypercorn
import hypercorn.protocol

INTERCEPTED_H2 = None
o_h2ProtocolInit = hypercorn.protocol.h2.H2Protocol.__init__


def h2ProtocolProxy(self, *args, **kwargs):
    global INTERCEPTED_H2
    o_h2ProtocolInit(self, *args, **kwargs)
    INTERCEPTED_H2 = self


hypercorn.protocol.h2.H2Protocol.__init__ = h2ProtocolProxy
config = Config()
config.bind = ["localhost:8080"]


def terminateConnection(protocol: hypercorn.protocol.h2.H2Protocol):
    protocol.connection.close_connection()


async def app(scope, receive, send):
    global INTERCEPTED_H2
    terminateConnection(INTERCEPTED_H2)


asyncio.run(serve(app, config))
