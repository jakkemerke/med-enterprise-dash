import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")),
)

from med_enterprise_dash.routes import get_home_route_name
from med_enterprise_dash.views.home import get_home_view


class TestHome(unittest.TestCase):
    def test_get_home_route_name(self):
        assert get_home_route_name() == "Home"

    def test_get_home_view(self):
        get_home_view(None)


if __name__ == "__main__":
    print(__name__)
