from typing import List


def add_wait_option_if_needed(wait: int = None) -> List[str]:
    return [] if wait is None else ['--wait', str(wait)]
