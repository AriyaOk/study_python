import mimetypes
import random

from framework.consts import dir_static


def application(environ, start_response):
    url = environ["PATH_INFO"]
    file_names = {
        "/xxx/": "styles.css",
        "/logo.png/": "ariyaOk.gif",
        "/": "index.html",
    }
    file_name = file_names.get(
        url,
    )

    if file_name is not None:
        status = "200 OK"
        type_file_ = mimetypes.guess_type(file_name)[0]
        headers = {
            "Content-type": type_file_,
        }
        payload = read_static(file_name)
    else:
        status = "404 not found"
        headers = {
            "Content-type": "text/plain",
        }
        payload = generate_404(environ)

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

    msg = f"Error! Your path: {url}. Pin: {pin}"

    return msg.encode()
