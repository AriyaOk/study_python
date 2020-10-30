import mimetypes

from framework.types import Response_T_
from framework.utils import read_static

filename_style = "styles.css"


def handle_style(_environ) -> Response_T_:
    payload = read_static(filename_style)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_style)[0]
    headers = {
        "Content-type": type_file_,
    }

    response = Response_T_(
        status=status,
        headers=headers,
        payload=payload,
    )
    return response
