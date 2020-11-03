import mimetypes

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static

filename_logo = "ariyaOk.gif"


def handle_logo(request: RequestT) -> ResponseT:
    payload = read_static(filename_logo)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_logo)[0]
    headers = {
        "Content-type": type_file_,
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=payload,
    )

    return response
