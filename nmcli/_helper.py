from typing import List


def add_wait_option_if_needed(wait: int = None) -> List[str]:
    return [] if wait is None else ['--wait', str(wait)]

def add_fields_option_if_needed(fields: str = None) -> List[str]:
    return [] if fields is None else ['-f', fields]
