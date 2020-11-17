from http.cookies import SimpleCookie
from typing import Dict
from typing import Optional
from urllib.parse import parse_qs

from framework import settings
from framework.consts import dir_static
from framework.consts import USER_COOKIE
from framework.consts import USER_TTL


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
    ln = int(environ.get("CONTENT_LENGTH") or 0)
    if ln == 0:
        return b""
    body = fp.read(ln)
    return body


def get_user_id(headers: Dict) -> Optional[str]:
    cookies_heders = headers.get("COOKIE", "")
    cookies = SimpleCookie(cookies_heders)  # parse_qs(headers.get("COOKIE", ""))
    if USER_COOKIE not in cookies:
        return None

    user_id = cookies[USER_COOKIE].value

    # user_id = cookies.get(USER_COOKIE, [None])[0]

    return user_id


def cookies_headers(user_id, del_coocies=False):
    cookies = SimpleCookie()

    cookies[USER_COOKIE] = user_id
    cookie = cookies[USER_COOKIE]
    cookie["Domain"] = settings.HOST
    cookie["Path"] = "/"
    cookie["HttpOnly"] = True
    if del_coocies:
        cookie["Max-Age"] = 0
    else:
        cookie["Max-Age"] = USER_TTL.total_seconds()

    cookie = str(cookies).split(":")[1].strip()

    return cookie
