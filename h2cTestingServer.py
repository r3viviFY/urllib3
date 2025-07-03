from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio
config = Config()
config.bind = ["localhost:8080"]
async def app(scope, receive, send):
    print(scope["headers"])
    await send({"type": "http.response.start", "status": 200, "headers": []})
    await send({"type": "http.response.body", "body": b"Hello, World!"})
asyncio.run(serve(app, config))