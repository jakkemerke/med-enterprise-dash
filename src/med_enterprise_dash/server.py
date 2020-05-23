from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

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
        config.include("routes.includeme", route_prefix="")
        config.include("apps.routes.includeme", route_prefix="/apps")
        app = config.make_wsgi_app()
    server = make_server(get_hostname(), get_port(), app)  # http://localhost:6543/
    server.serve_forever()
