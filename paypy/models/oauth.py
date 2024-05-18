from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class Oauth2ParHeaderBase:
    result_code: str
    result_message: str


@dataclass(slots=True, kw_only=True)
class Oauth2ParPayloadBase:
    request_uri: str
    expires_in: int
    expired_at: str


@dataclass(slots=True, kw_only=True)
class Oauth2ParResponseBase:
    header: Oauth2ParHeaderBase | None = None
    payload: Oauth2ParPayloadBase | None = None
