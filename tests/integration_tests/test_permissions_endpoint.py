import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")),
)

from med_enterprise_dash.micro_services.permissions import (
    get_apps_routes,
    get_permissions,
)


class TestPermissionsEndpoint(unittest.TestCase):
    def test_get_apps_list(self):
        permissions_dict = get_permissions("admin")

        print(f"Integration test: {__name__}")
        print(get_apps_routes(permissions_dict))
        print("")


if __name__ == "__main__":
    print(__name__)
