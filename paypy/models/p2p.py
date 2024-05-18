from dataclasses import dataclass
from enum import Enum, unique


@dataclass(slots=True, kw_only=True)
class AcceptP2PSendMoneyLinkRequestModel:
    request_id: str
    order_id: str
    verification_code: str
    passcode: int | None
    sender_message_id: str | None
    sender_channel_url: str | None


@dataclass(slots=True, kw_only=True)
class P2PLinkInfoRequestParamModel:
    verification_code: str


@unique
class P2PMoneyTransferStatus(Enum):
    CREATED = 0
    PENDING = 1
    COMPLETED = 2
    REJECTED = 3
    CANCELLED = 4
    EXPIRED = 5
    FAILED = 6


@dataclass(slots=True, kw_only=True)
class PendingP2PInfoModel:
    order_id: str
