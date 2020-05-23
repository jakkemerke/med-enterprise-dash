def get_port():
    return 6543


def get_hostname():
    return "localhost"


def get_host_url():
    return f"{get_hostname()}:{get_port()}"


def get_profile_route_name():
    return "Profile"


def get_apps_route_name():
    return "Apps"


def get_login_route_name():
    return "Login"


def get_home_route_name():
    return "Home"


def get_logout_callback_route_name():
    return "logout_callback"


def get_username(request):
    if request.session:
        return request.session["username"]
    else:
        return ""


def has_username(username):
    return username and username != ""


def is_logged_in(request):
    return has_username(get_username(request))
