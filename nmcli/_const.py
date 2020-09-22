from enum import Enum

class NetworkManagerState(Enum):
    UNKNOWN = 'unknown'
    ASLEEP = 'asleep'
    CONNECTING = 'connecting'
    CONNECTED_LOCAL = 'connected (local only)'
    CONNECTED_SITE = 'connected (site only)'
    CONNECTED_GLOBAL = 'connected'
    DISCONNECTING = 'disconnecting'
    DISCONNECTED = 'disconnected'

class NetworkConnectivity(Enum):
    UNKNOWN = 'unknown'
    NONE = 'none'
    PORTAL = 'portal'
    LIMITED = 'limited'
    FULL = 'full'
