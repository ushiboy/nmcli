from dataclasses import dataclass

@dataclass(frozen=True)
class Connection:
    name: str
    uuid: str
    conn_type: str
    device: str
