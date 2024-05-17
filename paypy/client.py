import aiohttp


class BaseClient(object):
    
    def __init__(self):
        self._session = aiohttp.ClientSession()
    
    async def close(self):
        if not self._session.closed:
            await self._session.close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_t, exc_v, exc_tb):
        await self.close()


    async def _make_request(self):