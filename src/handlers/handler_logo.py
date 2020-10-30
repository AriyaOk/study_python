import mimetypes

from framework.types import Response_T_
from framework.utils import read_static

filename_logo = "ariyaOk.gif"


def handle_logo(_environ) -> Response_T_:
    payload = read_static(filename_logo)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_logo)[0]
    headers = {
        "Content-type": type_file_,
    }

    response = Response_T_(
        status=status,
        headers=headers,
        payload=payload,
    )

    return response
