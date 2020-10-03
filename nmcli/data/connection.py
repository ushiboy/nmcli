from __future__ import annotations
from typing import Dict, Optional
from dataclasses import dataclass
import re

ConnectionDetails = Dict[str, Optional[str]]
ConnectionOptions = Dict[str, str]

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

    @classmethod
    def parse(cls, text: str) -> Connection:
        m = re.search(r'^([\S\s]+)\s{2}(\S+)\s{2}(\S+)\s+(\S+)\s*', text)
        if m:
            name, uuid, conn_type, device = m.groups()
            return Connection(name.strip(), uuid, conn_type, device)
        raise ValueError('Parse failed [%s]' % text)
