import hmac
import hashlib

from .config import Configs


def calculate_hash(http_method: str,
                   endpoint: str,
                   payload: str | None = ""
                   ) -> str:
    return hmac.new(key=Configs.HMAC_KEY.encode(),
                    msg=(http_method + "" + endpoint + "" + "x-requester" + ":" + Configs.CLIENT_NAME + "" + payload).encode(),
                    digestmod=hashlib.sha256).hexdigest()
