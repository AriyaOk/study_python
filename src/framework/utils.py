from typing import Dict
from typing import Optional
from urllib.parse import parse_qs

from framework.consts import dir_static
from framework.consts import USER_COOKIE


def read_static(name_file: str) -> bytes:
    path = dir_static / name_file
    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def get_form_data(body: bytes) -> dict:
    qs = body.decode()
    form_data = parse_qs(qs or "")

    return form_data


def get_body(environ: dict) -> bytes:

    fp = environ["wsgi.input"]
    ln = int(environ["CONTENT_LENGTH"] or 0)
    if ln == 0:
        return b""
    body = fp.read(ln)
    return body


def get_user_id(headers: Dict) -> Optional[str]:
    cookies = parse_qs(headers.get("COOKIE", ""))
    user_id = cookies.get(USER_COOKIE, [None])[0]

    return user_id
