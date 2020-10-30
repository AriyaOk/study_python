from framework.utils import read_static
from framework.utils import T


def handle_index(_environ) -> T:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(body_=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    return status, headers, result
