import sys
import traceback

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handler_500(_request: RequestT = None) -> ResponseT:
    error_class, error, tb = sys.exc_info()

    filenames = "".join(
        f"""<p>File <a href="http://localhost:8000/s/{frame.f_code.co_filename}">{frame.f_code.co_filename}</a>, line {lineno}</p>"""
        for frame, lineno in traceback.walk_tb(tb)
    )

    # result = traceback.format_exc()
    document = f"""
            <h1>WASTED</h1>
            <hr>
            <p>
            {filenames}
            </p>
            <p>
            {error_class.__name__}: {error}
            </p>
        """
    base_html = read_static("_base.html").decode()
    result = base_html.format(body_=document)
    result = result.encode()

    status = "500 Internal Server Error"

    headers = {
        "Content-type": "text/html",
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=result,
    )

    return response
