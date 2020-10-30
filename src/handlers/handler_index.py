from framework.types import Response_T_
from framework.utils import read_static


def handle_index(_environ) -> Response_T_:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(body_=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    response = Response_T_(
        status=status,
        headers=headers,
        payload=result,
    )
    return response
