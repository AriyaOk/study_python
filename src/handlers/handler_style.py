import mimetypes

from framework.types import ResponseT
from framework.utils import read_static

filename_style = "styles.css"


def handle_style(_environ) -> ResponseT:
    payload = read_static(filename_style)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_style)[0]
    headers = {
        "Content-type": type_file_,
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=payload,
    )
    return response
