import random

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handler_404(request: RequestT) -> ResponseT:
    url = request.path
    pin = random.randint(1, 1000)

    msg_str = f"Error! Your path: {url}. Pin: {pin}"
    base_html = read_static("_base.html").decode()
    msg = base_html.format(body_=msg_str)
    msg = msg.encode()

    status = "404 not found"

    headers = {
        "Content-type": "text/html",
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=msg,
    )

    return response
