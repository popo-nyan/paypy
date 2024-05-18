import os
import random
import aiohttp

from .models import (DeviceInfoBaseModel)
from .utils import (load_json_file)


class BaseClient(object):

    def __init__(self):
        self.__session = aiohttp.ClientSession()
        self._current_path = os.path.dirname(__file__)

    async def close(self):
        if not self.__session.closed:
            await self.__session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_t, exc_v, exc_tb):
        await self.close()

    async def _make_request(self,
                            method: str,
                            host: str,
                            route: str,
                            params: str | None = None,
                            payload: str | None = None,
                            headers: str | None = None,
                            ) -> aiohttp.ClientResponse:
        pass

    async def _construct_device_info(self,
                                     select_index: int | None = None) -> DeviceInfoBaseModel:
        devices_info = await load_json_file(self._current_path + "/devices.json")
        if select_index is None:
            device_info = random.choice(devices_info['samsung'])
        else:
            device_info = devices_info[select_index]
        return DeviceInfoBaseModel(device_name=device_info['modelName'],
                                   device_hardware_name=device_info['hardwareName'],
                                   device_manufacturer_name=device_info['deviceBrandName'],
                                   client_os_type='Android',
                                   client_os_version=device_info['osVersion'],
                                   client_os_release_version=device_info['osReleaseVersion'])
