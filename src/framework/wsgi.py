import mimetypes

from framework.consts import dir_static


def application(environ, start_response):
    url = environ["PATH_INFO"]
    file_names = {
        "/xxx/": "styles.css",
        "/logo.png/": "ariyaOk.gif",
    }
    file_name = file_names.get(url, "index.html")
    status = "200 OK"
    type_file_ = mimetypes.guess_type(file_name)[0]
    headers = {
        "Content-type": type_file_,
    }
    payload = read_static(file_name)

    start_response(status, list(headers.items()))
    yield payload


def read_static(name_file: str) -> bytes:
    path = dir_static / name_file
    with path.open("rb") as fp:
        payload = fp.read()

    return payload


#############################################################
