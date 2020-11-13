import dataclasses
import json
from typing import Dict

from framework.consts import file_user_db
from framework.types import UserT


def find_user(user_id: str) -> UserT:
    anonymous = UserT()

    if not user_id:
        return anonymous

    all_users = _load_all_users()
    user_params = all_users.get(user_id)
    if not user_params:
        return anonymous

    user_params = {"id": user_id, **user_params}

    user = UserT(**user_params)
    user.fix()

    if user.expired:
        return anonymous

    return user


def save_user(user: UserT):
    user.fix()
    user_params = dataclasses.asdict(user, dict_factory=UserT.dict_factory)

    all_users = _load_all_users()
    all_users.update(
        {
            user.id: user_params,
        }
    )

    _store_all_users(all_users)


def _load_all_users() -> Dict:
    data = {}

    try:
        with file_user_db.open("r") as fp:
            data = json.load(fp)
    except (IOError, json.JSONDecodeError):
        pass

    return data


def _store_all_users(users: Dict) -> None:
    with file_user_db.open("w") as fp:
        json.dump(users or {}, fp, sort_keys=True, indent=2)
