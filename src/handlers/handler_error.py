import random

from framework.types import Response_T_
from framework.utils import read_static


def handler_404(environ):
    url = environ["PATH_INFO"]
    pin = random.randint(1, 1000)

    msg_str = f"Error! Your path: {url}. Pin: {pin}"
    base_html = read_static("_base.html").decode()
    msg = base_html.format(body_=msg_str)
    msg = msg.encode()

    status = "404 not found"

    headers = {
        "Content-type": "text/html",
    }

    response = Response_T_(
        status=status,
        headers=headers,
        payload=msg,
    )

    return response
