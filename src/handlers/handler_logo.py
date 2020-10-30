import mimetypes

from framework.types import Response_Tuple
from framework.utils import read_static

filename_logo = "ariyaOk.gif"


def handle_logo(_environ) -> Response_Tuple:
    payload = read_static(filename_logo)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_logo)[0]
    headers = {
        "Content-type": type_file_,
    }

    return status, headers, payload
