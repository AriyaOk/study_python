import mimetypes
import random

from framework.consts import dir_static


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {
        "/": handle_index,
    }

    handler = handlers.get(url, generate_404)

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = handler(environ)

    start_response(status, list(headers.items()))
    yield payload


def read_static(name_file: str) -> bytes:
    path = dir_static / name_file
    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def generate_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pin = random.randint(1, 1000)

    msg_str = f"Error! Your path: {url}. Pin: {pin}"
    base_html = read_static("_base.html").decode()
    msg = base_html.format(body_=msg_str)
    return msg.encode()


def handle_index(_environ) -> bytes:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(body_=index_html)

    return result.encode()
