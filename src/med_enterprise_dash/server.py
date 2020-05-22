from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from routes.routes import *
from utils import get_port, get_hostname
from apps.routes import includeme

# import os, sys
# if "med_enterprise_dash" not in sys.path:
#     sys.path.insert(0, os.path.abspath("."))

if __name__ == "__main__":
    my_session_factory = SignedCookieSessionFactory("todo_add_a_secret")
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.set_session_factory(my_session_factory)
        config.add_static_view(path="med_enterprise_dash:static", name="static")

        config.add_route(get_home_route_name(), "/")
        config.add_view(
            get_home_view,
            route_name=get_home_route_name(),
            renderer="./templates/home.jinja2",
        )

        config.add_route(get_login_route_name(), "/login")
        config.add_view(login, route_name=get_login_route_name())

        config.add_route("logout", "/logout")
        config.add_view(logout, route_name="logout")
        config.add_route(get_logout_callback_route_name(), "/logout_callback")
        config.add_view(
            logout_callback,
            route_name=get_logout_callback_route_name(),
            renderer="./templates/logout_callback.jinja2",
        )

        config.add_route(get_profile_route_name(), "/profile")
        config.add_view(
            profile,
            route_name=get_profile_route_name(),
            renderer="./templates/profile.jinja2",
        )

        config.add_route(get_apps_route_name(), "/apps")
        config.add_view(
            apps, route_name=get_apps_route_name(), renderer="./templates/apps.jinja2"
        )

        config.include('apps.routes.includeme', route_prefix='/apps')

        app = config.make_wsgi_app()
    server = make_server(get_hostname(), get_port(), app)  # http://localhost:6543/
    server.serve_forever()
