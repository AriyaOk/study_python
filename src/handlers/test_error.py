from framework.types import RequestT
from framework.types import ResponseT


def make_error(_request: RequestT = None) -> ResponseT:
    1 / 0
