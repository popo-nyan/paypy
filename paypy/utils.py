import hmac
import json
import hashlib
import aiofiles

from urllib.parse import urlparse

from .config import Configs


def calculate_hash(http_method: str,
                   endpoint: str,
                   payload: str | None = "") -> str:
    """
    Hashを計算します。
    :param http_method: GET or POST or PUT
    :param endpoint:  /v1/config
    :param payload:
    :return:
    """
    return hmac.new(key=Configs.HMAC_KEY.encode(),
                    msg=(http_method + "" + endpoint + "" +
                         "x-requester" + ":" + Configs.CLIENT_NAME + "" + payload).encode(),
                    digestmod=hashlib.sha256).hexdigest()


async def load_json_file(file_path: str):
    """
    JSONファイルを読み込みます。
    :param file_path: ./device.json
    :return: {'samsung' : [...]}
    """
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        load_data = await file.read()
    return json.loads(load_data)


def parse_p2p_money_link(link: str) -> str:
    """
    PayPayの送金リンクからverificationCodeを抽出します。
    :param link: https://pay.paypay.ne.jp/hogehogehoge
    :return:  hogehogehoge
    """
    return urlparse(link).path.strip("/")
