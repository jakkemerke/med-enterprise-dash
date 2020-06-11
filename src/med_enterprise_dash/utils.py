from med_config import get_med_config


def get_port(med_config=get_med_config()):
    return med_config["port"]


def get_hostname(med_config=get_med_config()):
    return med_config["host"]


def get_scheme(med_config=get_med_config()):
    return med_config["scheme"]


def get_home_url_port(port):
    return "" if port == "" else f":{port}"


def get_home_url_scheme(scheme):
    return "" if scheme == "" else f"{scheme}://"


def get_host_url(med_config):
    return f"{get_home_url_scheme(get_scheme(med_config))}{get_hostname()}{get_home_url_port(get_port(med_config))}"


def get_home_path(med_config=get_med_config()):
    return med_config["home_path"]


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
