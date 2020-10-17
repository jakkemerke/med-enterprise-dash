import os, sys
import unittest


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src/med_enterprise_dash")
    ),
)

from __init__ import __version__
from auth import get_cas_client
from config import get_hostname
from routes import get_route_root
from server import get_session_factory
from utils.session import has_username
from utils.toml import get_med_config


class TestVersion(unittest.TestCase):
    def test_version(self):
        assert __version__ == "0.1.0"


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
    print("stub test")
