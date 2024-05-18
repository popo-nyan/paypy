import hmac
import json
import hashlib
import aiofiles

from .config import Configs


def calculate_hash(http_method: str,
                   endpoint: str,
                   payload: str | None = "") -> str:
    return hmac.new(key=Configs.HMAC_KEY.encode(),
                    msg=(http_method + "" + endpoint + "" +
                         "x-requester" + ":" + Configs.CLIENT_NAME + "" + payload).encode(),
                    digestmod=hashlib.sha256).hexdigest()


async def load_json_file(file_path: str):
    async with aiofiles.open(file_path, mode="r") as file:
        load_data = await file.read()
    return json.loads(load_data)
