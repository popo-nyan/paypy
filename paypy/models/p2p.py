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
    created = 0
    pending = 1
    completed = 2
    rejected = 3
    cancelled = 4
    expired = 5
    failed = 6


@dataclass(slots=True, kw_only=True)
class PendingP2PInfoModel:
    order_id: str


@dataclass(slots=True, kw_only=True)
class P2PUserModel:
    custom_display_name: str
    display_name: str
    external_user_id: str
    icon_image_url: str


@dataclass(slots=True, kw_only=True)
class P2PUserProfileModel:
    display_name: str
    photo_url: str
    external_id: str
    custom_display_name: str
    is_receiver: bool


@dataclass(slots=True, kw_only=True)
class P2PThemeListModel:
    theme_id: str
    theme_title: str
    icon_image_url: str
    pending_thumbnail_animation_url: str
    thumbnail_animation_url: str
    background_animation_url: str
    open_animation_url: str
    is_show_dark_background: bool
    should_hide_amount: bool


@dataclass(slots=True, kw_only=True)
class P2PSubWalletSplitModel:
    sender_emoney_amount: int
    sender_prepaid_amount: int
    receiver_emoney_amount: int
    receiver_prepaid_amount: int


@dataclass(slots=True, kw_only=True)
class P2PMessageDataModel:
    type: str
    isLink: bool
    requestId: str
    requestMoneyId: str | None = None
    orderId: str
    orderType: str
    transactionAt: str
    expiry: str
    status: str
    amount: int
    theme: P2PThemeListModel | None = None
    isQr: bool
    subWalletSplit: P2PSubWalletSplitModel | None = None
    sendMoneyLink: str
    sendMoneyLinkPasscode: str


@dataclass(slots=True, kw_only=True)
class P2PMessageInfoAPIModel:
    messageId: str
    messageType: str
    customType: str
    message: str
    chatRoomId: str
    user: P2PUserModel
    isRemoved: bool
    iosMinimumVersion: str
    androidMinimumVersion: str
