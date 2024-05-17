import time
from enum import Enum, unique


@unique
class PayPayLang(Enum):
    JA_JP = "ja"
    EN_US = "en"


class Configs:
    CLIENT_NAME = "android-pp"
    HMAC_KEY = "717198a8bcf3405384abcb4815d1efb9"
    
    APP_HEADERS = {'Host': 'app4.paypay.ne.jp',
                   'Client-Os-Type': None,
                   'Device-Acceleration-2': None,
                   'Device-Name': None,
                   'Is-Emulator': 'false',
                   'Device-Rotation': None,
                   'Device-Manufacturer-Name': None,
                   'Client-Os-Version': None,
                   'Device-Brand-Name': 'Android',
                   'Device-Orientation': None,
                   'Device-Acceleration': None,
                   'Device-Rotation-2': None,
                   'Client-Os-Release-Version': None,
                   'Client-Type': 'PAYPAYAPP',
                   'Device-Hardware-Name': None,
                   'Device-Orientation-2': None,
                   'Network-Status': None,
                   'Client-Version': None,
                   'Client-Mode': 'NORMAL',
                   'System-Locale': 'ja',
                   'Timezone': 'Asia/Tokyo',
                   'User-Agent': None,
                   'Accept-Charset': 'UTF-8',
                   'Accept': '*/*'}
    
    PUSH_HEADERS = {'Host': 'push-config.paypay.ne.jp',
                    'Content-Type': 'application/json',
                    'Cache-Control': 'no-cache',
                    'X-Requester': CLIENT_NAME,
                    'User-Agent': 'okhttp/4.11.0'}
    
    MAIN_HEADERS = {'Host': 'www.paypay.ne.jp',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                    'Accept': 'application/json, text/plain, */*',
                    'Client-Type': 'PAYPAYAPP',
                    'Client-App-Load-Start': str(time.time_ns())[:13],
                    'Client-Id': 'pay2-mobile-app-client',
                    'User-Agent': None,
                    'Baggage': 'sentry-environment=Production,sentry-release=4.21.0',
                    'X-Requested-With': 'jp.ne.paypay.android.app',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://www.paypay.ne.jp/portal/oauth2/sign-in?client_id=pay2-mobile-app-client&mode=landing',
                    'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7'}


class Endpoints:
    APP_HOST = "https://app4.paypay.ne.jp/"
    WEB_HOST = "https://www.paypay.ne.jp/"
    PRS_HOST = "https://prs.paypay.ne.jp/"
    PUSH_HOST = "https://push-config.paypay.ne.jp/"
    
    PRS_V1 = PRS_HOST + "v1/api/"
    PRS_V2 = PRS_HOST + "v2/api/"
    
    BFF_V1 = APP_HOST + "bff/v1/"
    BFF_V2 = APP_HOST + "bff/v2/"
    BFF_V3 = APP_HOST + "bff/v3/"
    
    PUSH_V1 = PUSH_HOST + "v1/"
    
    PORTAL_V2 = WEB_HOST + "portal/api/v2/"
