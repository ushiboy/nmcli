from dataclasses import dataclass

@dataclass(frozen=True)
class Hotspot:
    ifname: str
    con_name: str
    ssid: str
    band: str
    channel: int
    password: str

    def to_json(self):
        return {
            'ifname': self.ifname,
            'con_name': self.con_name,
            'ssid': self.ssid,
            'band': self.band,
            'channel': self.channel,
            'password': self.password
        }
