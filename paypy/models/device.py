from enum import Enum, unique
from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class DeviceInfoBaseModel:
    device_name: str
    device_hardware_name: str
    device_manufacturer_name: str
    client_os_version: str
    client_os_type: str
    client_os_release_version: str


@unique
class DeviceLockType(Enum):
    biometric_strong = "BIOMETRIC_STRONG"
    biometric_weak = "BIOMETRIC_WEAK"
    pin = "DEVICE"
    none = "NONE"


@unique
class DeviceNetworkStatus(Enum):
    wifi = 0
    mobile = 1
    no_connection = 2
