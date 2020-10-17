from typing import Any


def get_username(request: Any) -> str:
    if request and request.session and hasattr(request, "session"):
        return request.session["username"]
    else:
        return ""


def has_username(username: str) -> bool:
    return username != None and type(username) is str and username != ""


def is_logged_in(request: Any) -> bool:
    return has_username(get_username(request))
