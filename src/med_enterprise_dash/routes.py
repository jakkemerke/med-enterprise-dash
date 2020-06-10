from views import *


def get_home_path(med_config):
    return med_config["home_path"]


def includeme(config):
    home_path = get_home_path(get_med_config())
    config.add_route(get_home_route_name(), home_path)
    config.add_view(
        get_home_view,
        route_name=get_home_route_name(),
        renderer="./templates/home.jinja2",
    )

    config.add_route(get_login_route_name(), f"{home_path}login")
    config.add_view(login, route_name=get_login_route_name())

    config.add_route("logout", f"{home_path}logout")
    config.add_view(logout, route_name="logout")

    config.add_route(get_logout_callback_route_name(), f"{home_path}logout_callback")
    config.add_view(
        logout_callback,
        route_name=get_logout_callback_route_name(),
        renderer="./templates/logout_callback.jinja2",
    )

    config.add_route(get_profile_route_name(), f"{home_path}profile")
    config.add_view(
        profile,
        route_name=get_profile_route_name(),
        renderer="./templates/profile.jinja2",
    )

    config.add_route(get_apps_route_name(), f"{home_path}apps")
    config.add_view(
        apps, route_name=get_apps_route_name(), renderer="./templates/apps.jinja2"
    )
