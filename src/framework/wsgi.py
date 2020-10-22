import mimetypes

from framework.consts import dir_static
from framework.consts import file_index
from framework.consts import file_logo
from framework.consts import file_scc


def application(environ, start_response):
    url = environ["PATH_INFO"]
    if url == "/xxx/":
        status = "200 OK"
        # headers = {
        #    "Content-type": "text/css",
        # }
        # payload = read_from_styles_css()

        # type_file_ = mimetypes.guess_type(file_scc)[0]
        headers = set_headers(file_scc)  # "text/css"
        payload = read_from_file(file_scc, "r", True)  # read_from_styles_css()

        start_response(status, list(headers.items()))

        yield payload
        # return None #можно без None - функции, если не указано явно, то возвращает None
    elif url == "/logo.png/":
        status = "200 OK"
        # headers = {
        #    "Content-type": "image/png",
        # }
        # payload = read_from_styles_png()

        # type_file_ = mimetypes.guess_type(file_logo)[0]
        headers = set_headers(file_logo)  # "image/png"
        payload = read_from_file(file_logo, "rb", False)  # read_from_styles_png()

        start_response(status, list(headers.items()))

        yield payload
    else:
        status = "200 OK"
        # headers = {
        #    "Content-type": "text/html",
        # }
        # payload = read_from_index_html()

        # type_file_ = mimetypes.guess_type(file_index)[0]
        headers = set_headers(file_index)  # "text/html"
        payload = read_from_file(file_index, "r", True)  # read_from_index_html()

        start_response(status, list(headers.items()))

        yield payload


def read_from_file(name_file, mode, encode_use):
    path = dir_static / name_file
    with path.open(mode) as fp:
        payload = fp.read()

    if encode_use:
        payload = payload.encode()

    return payload


def set_headers(file_name):
    type_file_ = mimetypes.guess_type(file_name)[0]
    headers = {
        "Content-type": type_file_,
    }
    return headers


#############################################################
def read_from_index_html():
    path = dir_static / "index.html"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_styles_css():
    path = dir_static / "styles.css"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_styles_png():
    path = dir_static / "logo.png"
    with path.open("rb") as fp:
        payload = fp.read()

    return payload
