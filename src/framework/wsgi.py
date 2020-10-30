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
    url = environ["PATH_INFO"]

    handler = handlers_.get(url, handler_404)

    response = handler(environ)

    start_response(response.status, list(response.headers.items()))
    yield response.payload
