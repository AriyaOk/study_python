from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handle_hello(request: RequestT) -> ResponseT:
    name = (request.query.get("name") or [None])[0]
    base_html = read_static("_base.html").decode()
    index_html = read_static("hello_html.html").decode()  # f"<h1>Hello {name}</h1>"
    index_html = index_html.format(name_hader=name or "anon", name_value=name or "")
    result = base_html.format(body_=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=result,
    )
    return response
