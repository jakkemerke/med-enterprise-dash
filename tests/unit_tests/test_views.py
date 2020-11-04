import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")),
)

from pyramid.request import Request

from med_enterprise_dash.routes import get_home_route_name
from med_enterprise_dash.views.apps import apps, get_apps_response
from med_enterprise_dash.views.home import get_home_view
from med_enterprise_dash.views.login import login, get_next, get_cas_client
from med_enterprise_dash.views.logout import logout, get_cas_client
from med_enterprise_dash.views.logout_callback import (
    logout_callback,
    get_logout_callback_response,
)
from med_enterprise_dash.views.profile import (
    profile,
    get_url_to_login,
    get_profile_response,
)


class TestHome(unittest.TestCase):
    def test_get_home_route_name(self):
        assert get_home_route_name() == "Home"

    def test_get_home_view(self):
        get_home_view(None)


class TestLogin(unittest.TestCase):

    # def test_login(self):
    #     login(Request({}))

    def test_get_next(self):
        get_next(Request({}))


class TestProfile(unittest.TestCase):

    # def test_profile(self):
    #     profile(Request({}))

    # def test_get_url_to_login(self):
    #     get_url_to_login(Request({}))

    def test_get_profile_response(self):
        get_profile_response(None)


# class TestLogout(unittest.TestCase):

#     def test_logout(self):
#         logout(Request({}))


class TestLogoutCallback(unittest.TestCase):

    # def test_logout_callback(self):
    #     logout(Request({}))

    def test_get_logout_callback_response(self):
        get_logout_callback_response()


class TestApps(unittest.TestCase):

    # def test_apps(self):
    #     apps(Request({}))

    def test_get_apps_response(self):
        get_apps_response(None)
