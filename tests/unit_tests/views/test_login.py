import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")),
)

from pyramid.request import Request

from med_enterprise_dash.views.login import login, get_next, get_cas_client


class TestLogin(unittest.TestCase):
    def test_get_next(self):
        get_next(Request({}))


if __name__ == "__main__":
    print(__name__)
