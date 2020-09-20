from enum import Enum

class NetworkConnectivity(Enum):
    UNKNOWN = 'unknown'
    NONE = 'none'
    PORTAL = 'portal'
    LIMITED = 'limited'
    FULL = 'full'
