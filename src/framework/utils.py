from typing import Tuple

from framework.consts import dir_static

T = Tuple[str, dict, bytes]


def read_static(name_file: str) -> bytes:
    path = dir_static / name_file
    with path.open("rb") as fp:
        payload = fp.read()

    return payload
