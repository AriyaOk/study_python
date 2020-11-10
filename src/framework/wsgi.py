from urllib.parse import parse_qs

from framework.types import RequestT
from framework.utils import get_body
from framework.utils import get_form_data
from handlers import handle_hello
from handlers import handle_index
from handlers import handle_logo
from handlers import handle_style
from handlers import handler_404
from handlers import handler_500
from handlers.test_error import make_error

handlers_ = {
    "/logo.png/": handle_logo,
    "/xxx/": handle_style,
    "/": handle_index,
    "/e": make_error,
    "/h": handle_hello,
}


def application(environ, start_response):
    try:
        path = environ["PATH_INFO"]

        handler = handlers_.get(path, handler_404)

        body = get_body(environ)
        form_data = get_form_data(body)

        request_key_http = filter(lambda key: key.startswith("HTTP"), environ)

        request_headers = {key[5:]: environ[key] for key in request_key_http}

        request = RequestT(
            method=environ["REQUEST_METHOD"],
            path=path,
            headers=request_headers,
            query=parse_qs(environ.get("QUERY_STRING") or ""),
            body=body,
            form_data=form_data,
        )
        response = handler(request)
    except:
        response = handler_500()

    start_response(response.status, list(response.headers.items()))
    yield response.payload
