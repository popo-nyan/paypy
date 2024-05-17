from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class Oauth2ParHeaderBase:
    resultCode: str
    resultMessage: str


@dataclass(slots=True, kw_only=True)
class Oauth2ParPayloadBase:
    requestUri: str
    expiresIn: int
    expiredAt: str


@dataclass(slots=True, kw_only=True)
class Oauth2ParBase:
    header: Oauth2ParHeaderBase | None = None
    payload: Oauth2ParPayloadBase | None = None
