import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")),
)

from med_enterprise_dash.views.apps import apps, get_apps_response


class TestApps(unittest.TestCase):
    def test_get_apps_response(self):
        get_apps_response(None)


if __name__ == "__main__":
    print(__name__)
