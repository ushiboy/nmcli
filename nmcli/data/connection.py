from dataclasses import dataclass


@dataclass(frozen=True)
class Connection:
    name: str
    uuid: str
    conn_type: str
    device: str

    def to_json(self):
        return {
            'name': self.name,
            'uuid': self.uuid,
            'conn_type': self.conn_type,
            'device': self.device
        }
