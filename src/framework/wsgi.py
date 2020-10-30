from handlers.handler_error import handler_404
from handlers.handler_index import handle_index
from handlers.handler_logo import handle_logo
from handlers.handler_style import handle_style

handlers_ = {
    "/logo.png/": handle_logo,
    "/xxx/": handle_style,
    "/": handle_index,
}


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handler = handlers_.get(url, handler_404)

    status, headers, payload = handler(environ)
    assert isinstance(payload, bytes), url

    start_response(status, list(headers.items()))
    yield payload
