import mimetypes

from framework.utils import read_static
from framework.utils import T

filename_style = "styles.css"


def handle_style(_environ) -> T:
    payload = read_static(filename_style)

    status = "200 OK"

    type_file_ = mimetypes.guess_type(filename_style)[0]
    headers = {
        "Content-type": type_file_,
    }

    return status, headers, payload
