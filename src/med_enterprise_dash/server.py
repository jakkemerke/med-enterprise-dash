from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory
import pyramid.httpexceptions as exc

# import os, sys
# if "med_enterprise_dash" not in sys.path:
#     sys.path.insert(0, os.path.abspath("."))

# cas_client = CASClient(
#     version=3,
#     service_url='http://localhost:6543/login?next=%2Fprofile',
#     server_url='https://django-cas-ng-demo-server.herokuapp.com/cas/'
# )


def get_username(request):
    if request.session:
        return request.session["username"]
    else:
        return ""


def get_home_route_name():
    return "Home"


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
    }


def get_login_route_name():
    return "Login"


def login(request):
    request.session["username"] = "admin"
    raise exc.HTTPFound(request.route_url(get_profile_route_name()))


def logout(request):
    request.session.invalidate()
    raise exc.HTTPFound(request.route_url(get_home_route_name()))


def apps(request):
    return {"name": "Apps"}


def get_profile_route_name():
    return "Profile"


def profile(request):
    session = request.session
    if "username" in session:
        return {
            "name": get_profile_route_name(),
            "username": get_username(request),
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))


if __name__ == "__main__":
    my_session_factory = SignedCookieSessionFactory("todo_add_a_secret")
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.set_session_factory(my_session_factory)

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

        config.add_route(get_profile_route_name(), "/profile")
        config.add_view(
            profile,
            route_name=get_profile_route_name(),
            renderer="./templates/profile.jinja2",
        )

        config.add_route("apps", "/apps")
        config.add_view(apps, route_name="apps", renderer="./templates/apps.jinja2")

        app = config.make_wsgi_app()
    server = make_server("localhost", 6543, app)  # localhost:6543
    server.serve_forever()
