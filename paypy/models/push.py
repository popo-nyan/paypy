from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class PushConfigBase:
    ios_signal_endpoint: str
    ios_signal_dispatch_interval: str
    ios_signal_batch_size: str
    ios_signal_max_batch_size: str
    ios_push_registry_endpoint: str
    ios_inbox_endpoint: str
    ios_flash_endpoint: str
    ios_inbox_enabled: str
    android_push_registry_endpoint: str
    android_event_endpoint: str
    android_inbox_endpoint: str
    android_signal_batch_frequency: str
    android_is_inbox_enabled: str
    android_is_flash_enabled: str
    android_is_push_enabled: str
    android_event_batch_size: str
    flash_max_backgroud_elapsed_time: str
