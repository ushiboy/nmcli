from typing import List


def add_wait_option_if_needed(wait_sec: int = None) -> List[str]:
    return [] if wait_sec is None else ['--wait', str(wait_sec)]
