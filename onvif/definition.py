"""ONVIF Service Definitions"""

SERVICES = {
    "devicemgmt": {
        "ns": "http://www.onvif.org/ver10/device/wsdl",
        "wsdl": "www.onvif.org/ver10/device/wsdl/devicemgmt.wsdl",
        "binding": "DeviceBinding",
    },
    "media": {
        "ns": "http://www.onvif.org/ver10/media/wsdl",
        "wsdl": "www.onvif.org/ver10/media/wsdl/media.wsdl",
        "binding": "MediaBinding",
    },
    "media2": {
        "ns": "http://www.onvif.org/ver20/media/wsdl",
        "wsdl": "www.onvif.org/ver20/media/wsdl/media2.wsdl",
        "binding": "Media2Binding",
    },
    "ptz": {
        "ns": "http://www.onvif.org/ver20/ptz/wsdl",
        "wsdl": "www.onvif.org/ver20/ptz/wsdl/ptz.wsdl",
        "binding": "PTZBinding",
    },
    "imaging": {
        "ns": "http://www.onvif.org/ver20/imaging/wsdl",
        "wsdl": "www.onvif.org/ver20/imaging/wsdl/imaging.wsdl",
        "binding": "ImagingBinding",
    },
    "deviceio": {
        "ns": "http://www.onvif.org/ver10/deviceIO/wsdl",
        "wsdl": "www.onvif.org/ver10/deviceio.wsdl",
        "binding": "DeviceIOBinding",
    },
    "events": {
        "ns": "http://www.onvif.org/ver10/events/wsdl",
        "wsdl": "www.onvif.org/ver10/events/wsdl/event.wsdl",
        "binding": "EventBinding",
    },
    "pullpoint": {
        "ns": "http://www.onvif.org/ver10/events/wsdl",
        "wsdl": "www.onvif.org/ver10/events/wsdl/event.wsdl",
        "binding": "PullPointSubscriptionBinding",
    },
    "notification": {
        "ns": "http://www.onvif.org/ver10/events/wsdl",
        "wsdl": "www.onvif.org/ver10/events/wsdl/event.wsdl",
        "binding": "NotificationProducerBinding",
    },
    "subscription": {
        "ns": "http://www.onvif.org/ver10/events/wsdl",
        "wsdl": "www.onvif.org/ver10/events/wsdl/event.wsdl",
        "binding": "SubscriptionManagerBinding",
    },
    "analytics": {
        "ns": "http://www.onvif.org/ver20/analytics/wsdl",
        "wsdl": "www.onvif.org/ver20/analytics/wsdl/analytics.wsdl",
        "binding": "AnalyticsEngineBinding",
    },
    "recording": {
        "ns": "http://www.onvif.org/ver10/recording/wsdl",
        "wsdl": "www.onvif.org/ver10/recording.wsdl",
        "binding": "RecordingBinding",
    },
    "search": {
        "ns": "http://www.onvif.org/ver10/search/wsdl",
        "wsdl": "www.onvif.org/ver10/search.wsdl",
        "binding": "SearchBinding",
    },
    "replay": {
        "ns": "http://www.onvif.org/ver10/replay/wsdl",
        "wsdl": "www.onvif.org/ver10/replay.wsdl",
        "binding": "ReplayBinding",
    },
    "receiver": {
        "ns": "http://www.onvif.org/ver10/receiver/wsdl",
        "wsdl": "www.onvif.org/ver10/receiver.wsdl",
        "binding": "ReceiverBinding",
    },
}
