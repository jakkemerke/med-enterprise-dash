from views import *


def includeme(config):
    config.add_route(get_home_route_name(), "/")
    config.add_view(
        get_home_view,
        route_name=get_home_route_name(),
        renderer="./templates/home.jinja2",
    )

    config.add_route(get_login_route_name(), "/login/")
    config.add_view(login, route_name=get_login_route_name())

    config.add_route("logout", "/logout/")
    config.add_view(logout, route_name="logout")

    config.add_route(get_logout_callback_route_name(), "/logout_callback/")
    config.add_view(
        logout_callback,
        route_name=get_logout_callback_route_name(),
        renderer="./templates/logout_callback.jinja2",
    )

    config.add_route(get_profile_route_name(), "/profile/")
    config.add_view(
        profile,
        route_name=get_profile_route_name(),
        renderer="./templates/profile.jinja2",
    )

    config.add_route(get_apps_route_name(), "/apps/")
    config.add_view(
        apps, route_name=get_apps_route_name(), renderer="./templates/apps.jinja2"
    )
