import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")),
)

from med_enterprise_dash.__init__ import __version__
from med_enterprise_dash.auth import get_cas_client
from med_enterprise_dash.config import get_hostname
from med_enterprise_dash.routes import get_route_root
from med_enterprise_dash.server import get_session_factory
from med_enterprise_dash.utils.session import has_username
from med_enterprise_dash.utils.toml import get_med_config


class TestVersion(unittest.TestCase):
    def test_version(self):
        assert __version__ is not None


class TestConfig(unittest.TestCase):
    def test_toml(self):
        get_med_config()

    def test_get_hostname(self):
        get_hostname()


class TestAuth(unittest.TestCase):
    def test_get_auth_client(self):
        get_cas_client(get_med_config())


class TestRoutes(unittest.TestCase):
    def test_get_route_root(self):
        get_route_root()


class TestSession(unittest.TestCase):
    def test_has_username(self):
        assert has_username("foo") == True


class TestServer(unittest.TestCase):
    def test_get_session_factory(self):
        get_session_factory(get_med_config())


if __name__ == "__main__":
    print(__name__)
