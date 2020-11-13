from framework import settings
from framework.consts import file_user_db
from framework.consts import USER_COOKIE
from framework.consts import USER_TTL
from framework.db import save_user
from framework.types import RequestT
from framework.types import ResponseT
from framework.types import UserT
from framework.utils import read_static


def handle_hello(request: RequestT) -> ResponseT:
    method = request.method
    handlers_ = {
        "GET": handle_hello_get,
        "POST": handle_hello_post,
    }
    handler = handlers_.get(method)

    # if request.method == "GET":
    #     response = handle_hello_get(request)
    # else:
    #     response = handle_hello_post(request)
    response = handler(request)
    return response


def handle_hello_get(request: RequestT) -> ResponseT:
    assert request.method == "GET"

    # user_data = load_user_data(request)
    # name = user_data["name"]
    # adress = user_data["adress"]
    # name = (request.form_data.get("name") or [None])[0]
    # adress = (request.form_data.get("adress") or [None])[0]

    base_html = read_static("_base.html").decode()
    index_html = read_static("hello_html.html").decode()  # f"<h1>Hello {name}</h1>"

    index_html = index_html.format(
        name_hader=request.user.name or "anon",
        name_value=request.user.name or "",
        adress_hader=request.user.address or "anywhere",
        adress_value=request.user.address or "",
    )
    result = base_html.format(body_=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=result,
    )
    return response


def handle_hello_post(request: RequestT) -> ResponseT:
    assert request.method == "POST"

    form_data = request.form_data

    name = (form_data.get("name") or [None])[0]
    adress = (form_data.get("adress") or [None])[0]

    request.user.name = name
    request.user.address = adress

    save_user(request.user)
    status = "302 OK"
    headers = {
        "Location": "/h",
        "Set-Cookie": (
            f"{USER_COOKIE}={request.user.id};"
            f" Domain={settings.HOST};"
            f" HttpOnly;"
            f" Max-Age={USER_TTL.total_seconds()}"
        ),
    }

    response = ResponseT(
        status=status,
        headers=headers,
        payload=b"",
    )
    return response


# def save_user(request: RequestT) -> None:
#     dir_file = file_user_db
#     user_data = {
#         "name": request.user.name,
#         "adress": request.user.address,
#     }
#     user_id = build_user_id(request)
#
#     with dir_file.open("r") as fp:
#         users_id_dict = json.load( fp)
#
#     users_id_dict.update({
#         user_id: user_data,
#     })
#
#     with dir_file.open("w") as fp:
#         json.dump(users_id_dict, fp)


# def load_user_data(request: RequestT,) -> dict:
#     dir_file = file_user_db
#     if not dir_file.is_file():
#         return {
#             "name": "anon",
#             "adress": "xz",
#         }
#
#     with dir_file.open("r") as fp:
#         # name, adress = fp.readlines()
#         user_data = json.load(fp)
#
#     return user_data
