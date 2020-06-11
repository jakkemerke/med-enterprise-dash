from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from pyramid.httpexceptions import HTTPNotFound

from utils import (
    get_port,
    get_hostname,
    get_route_prefix,
    get_installation_subdirectory,
    get_static_path_offset,
)
from apps.routes import includeme
from med_config import get_med_config


def notfound(request):
    return HTTPNotFound()

def get_session_factory(med_config):
    return SignedCookieSessionFactory(med_config["session_factory"])


def get_app():
    with Configurator() as config:
        med_config = get_med_config()
        subdirectory = get_installation_subdirectory(med_config)
        route_prefix = get_route_prefix(subdirectory)
        path_offset = get_static_path_offset(subdirectory)

        config.include("pyramid_jinja2")
        config.set_session_factory(get_session_factory(med_config))
        config.add_static_view(
            path="med_enterprise_dash:static", name=f"{path_offset}static"
        )
        config.include("routes.includeme", route_prefix=f"{route_prefix}")
        config.include("apps.routes.includeme", route_prefix=f"{route_prefix}/apps")

        config.add_notfound_view(notfound, append_slash=True)
        return config.make_wsgi_app()


if __name__ == "__main__":
    # http://localhost:6543/
    server = make_server(get_hostname(), get_port(), get_app())
    server.serve_forever()
