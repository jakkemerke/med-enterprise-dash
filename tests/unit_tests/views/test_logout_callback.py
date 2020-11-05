import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")),
)

from med_enterprise_dash.views.logout_callback import get_logout_callback_response


class TestLogoutCallback(unittest.TestCase):
    def test_get_logout_callback_response(self):
        get_logout_callback_response()


if __name__ == "__main__":
    print(__name__)
