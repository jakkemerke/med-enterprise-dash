from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from utils import get_port, get_hostname, get_home_path
from apps.routes import includeme
from med_config import get_med_config


def get_session_factory(med_config=get_med_config()):
    return SignedCookieSessionFactory(med_config["session_factory"])


def get_app():
    with Configurator() as config:
        home_path = get_home_path(get_med_config())
        config.include("pyramid_jinja2")
        config.set_session_factory(get_session_factory())
        config.add_static_view(
            path="med_enterprise_dash:static", name=f"{home_path}static"
        )
        config.include("routes.includeme", route_prefix=f"{home_path}")
        config.include("apps.routes.includeme", route_prefix=f"/{home_path}apps")
        return config.make_wsgi_app()


if __name__ == "__main__":
    # http://localhost:6543/
    server = make_server(get_hostname(), get_port(), get_app())
    server.serve_forever()
