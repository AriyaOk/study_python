import random

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handler_404(request: RequestT) -> ResponseT:
    url_my = request.path
    pin_my = random.randint(1, 1000)

    teg_str_table = """<tr>
    <th>{key[0]}1</th>
    <th>{key[1]}</th>
   </tr>
    """
    teg_table = ""
    for key in request.headers:
        value = request.headers[key]
        teg_table = teg_table + teg_str_table.format(key=[key, value])

    # msg_str = f"Error! Your path: {url}. Pin: {pin}"
    base_html = read_static("_base.html").decode()
    msg_html = read_static("table.html").decode()
    msg_html = msg_html.format(dinamic=[url_my, pin_my, teg_table])

    result = base_html.format(body_=msg_html)
    result = result.encode()

    status = "404 not found"

    headers = {
        "Content-type": "text/html",
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=result,
    )

    return response
