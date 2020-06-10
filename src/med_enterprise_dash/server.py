from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from utils import get_port, get_hostname
from apps.routes import includeme

# import os, sys
# if "med_enterprise_dash" not in sys.path:
#     sys.path.insert(0, os.path.abspath("."))


def get_session_factory():
    return SignedCookieSessionFactory("todo_add_a_secret")


def get_app():
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.set_session_factory(get_session_factory())
        config.add_static_view(path="med_enterprise_dash:static", name="static")
        config.include("routes.includeme", route_prefix="")
        config.include("apps.routes.includeme", route_prefix="/apps")
        return config.make_wsgi_app()


if __name__ == "__main__":
    # http://localhost:6543/
    server = make_server(get_hostname(), get_port(), get_app())
    server.serve_forever()
