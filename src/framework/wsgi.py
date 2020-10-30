from framework.types import RequestT
from handlers import handle_index
from handlers import handle_logo
from handlers import handle_style
from handlers.handler_error import handler_404

handlers_ = {
    "/logo.png/": handle_logo,
    "/xxx/": handle_style,
    "/": handle_index,
}


def application(environ, start_response):
    path = environ["PATH_INFO"]

    handler = handlers_.get(path, handler_404)

    # keys = list(environ.keys())
    # request_key_http = [
    #     key
    #     for key in environ
    #     if key.startswith("HTTP")
    # ]
    request_key_http = filter(lambda key: key.startswith("HTTP"), environ)

    request_headers = {key[5:]: environ[key] for key in request_key_http}

    request = RequestT(
        method=environ["REQUEST_METHOD"],
        path=path,
        headers=request_headers,
    )
    response = handler(request)

    start_response(response.status, list(response.headers.items()))
    yield response.payload
