from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# import os, sys
# if "med_enterprise_dash" not in sys.path:
#     sys.path.insert(0, os.path.abspath("."))


def home(request):
    return {"name": "Home"}


def login(request):
    return Response("<body>Login stub...</body>")


def logout(request):
    return Response('<body>Go back <a href="/">home</a></body>')


def apps(request):
    return Response("<body>Apps stub...</body>")


if __name__ == "__main__":
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.add_route("home", "/")
        config.add_view(home, route_name="home", renderer="./templates/home.jinja2")
        config.add_route("logout", "/logout")
        config.add_view(logout, route_name="logout")
        config.add_route("login", "/login")
        config.add_view(login, route_name="login")
        config.add_route("apps", "/apps")
        config.add_view(apps, route_name="apps")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()
