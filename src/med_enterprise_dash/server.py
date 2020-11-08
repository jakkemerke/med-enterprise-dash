from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory, JSONSerializer
from pyramid.httpexceptions import HTTPNotFound

# TODO: Make this an enabled option via the toml config.
from pyramid.events import NewRequest

from med_enterprise_dash.config import (
    get_port,
    get_hostname,
    get_route_prefix,
    get_installation_subdirectory,
    get_static_path_offset,
)
from med_enterprise_dash.routes import *
from med_enterprise_dash.utils.toml import get_med_config
from med_enterprise_dash.views.appointments import get_appointments_view
from med_enterprise_dash.views.appointments_alternate import (
    get_appointments_alternate_view,
)
from med_enterprise_dash.views.apps import apps
from med_enterprise_dash.views.data_entry import get_data_entry_view
from med_enterprise_dash.views.events import get_events_view
from med_enterprise_dash.views.file_archive import get_file_archive_view
from med_enterprise_dash.views.home import get_home_view
from med_enterprise_dash.views.login import login
from med_enterprise_dash.views.login_verification import get_login_verification_view
from med_enterprise_dash.views.logout import logout
from med_enterprise_dash.views.logout_callback import logout_callback
from med_enterprise_dash.views.lookup import get_lookup_view
from med_enterprise_dash.views.portal import get_portal_view
from med_enterprise_dash.views.profile import profile
from med_enterprise_dash.views.status import get_status_view


def notfound(request):
    return HTTPNotFound()


def get_session_factory(med_config):
    return SignedCookieSessionFactory(
        med_config["session_factory"], serializer=JSONSerializer()
    )


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

        config.add_notfound_view(notfound, append_slash=True)

        # ======== HOME
        config.add_route(get_home_route_name(), get_route_root())
        config.add_view(
            get_home_view,
            route_name=get_home_route_name(),
            renderer="./templates/home.jinja2",
        )

        # ======== LOGIN
        config.add_route(get_login_route_name(), get_route_login())
        config.add_view(login, route_name=get_login_route_name())

        # ======== LOGIN_VERIFICATION
        config.add_route(
            get_login_verification_route_name(), get_route_login_verification()
        )
        config.add_view(
            get_login_verification_view,
            route_name=get_login_verification_route_name(),
            renderer="./templates/login_verification.jinja2",
        )

        # ======== LOGOUT
        config.add_route(get_logout_route_name(), get_route_logout())
        config.add_view(logout, route_name=get_logout_route_name())

        # ======== LOGOUT_CALLBACK
        config.add_route(get_logout_callback_route_name(), get_route_logout_callback())
        config.add_view(
            logout_callback,
            route_name=get_logout_callback_route_name(),
            renderer="./templates/logout_callback.jinja2",
        )

        # ======== PROFILE
        config.add_route(get_profile_route_name(), get_route_profile())
        config.add_view(
            profile,
            route_name=get_profile_route_name(),
            renderer="./templates/profile.jinja2",
        )

        # ======== APPS
        config.add_route(get_apps_route_name(), get_route_apps())
        config.add_view(
            apps, route_name=get_apps_route_name(), renderer="./templates/apps.jinja2"
        )

        # ========           =========================================
        # ======== FRONTENDS =========================================
        # ========           =========================================

        # ======== APPOINTMENTS APP
        config.add_route(get_appointments_route_name(), get_appointments_route())
        config.add_view(get_appointments_view, route_name=get_appointments_route_name())

        # ======== APPOINTMENTS_ALTERNATE APP
        config.add_route(
            get_appointments_alternate_route_name(), get_appointments_alternate_route()
        )
        config.add_view(
            get_appointments_alternate_view,
            route_name=get_appointments_alternate_route_name(),
            renderer="./templates/apps/appointments_alternate.jinja2",
        )
        config.add_static_view(
            path="med_enterprise_dash:static/med-appointments/css",
            name=f"apps/appointments_alternate/static/css",
        )
        config.add_static_view(
            path="med_enterprise_dash:static/med-appointments/js",
            name=f"apps/appointments_alternate/static/js",
        )

        # ======== DATA_ENTRY APP
        config.add_route(get_data_entry_route_name(), get_data_entry_route())
        config.add_view(
            get_data_entry_view,
            route_name=get_data_entry_route_name(),
            renderer="./templates/apps/data_entry.jinja2",
        )
        config.add_static_view(
            path="med_enterprise_dash:static/med-data-entry/css",
            name=f"apps/data_entry/static/css",
        )
        config.add_static_view(
            path="med_enterprise_dash:static/med-data-entry/js",
            name=f"apps/data_entry/static/js",
        )

        # ======== EVENTS APP
        config.add_route(get_events_route_name(), get_events_route())
        config.add_view(get_events_view, route_name=get_events_route_name())

        # ======== FILE_ARCHIVE APP
        config.add_route(get_file_archive_route_name(), get_file_archive_route())
        config.add_view(get_file_archive_view, route_name=get_file_archive_route_name())

        # ======== LOOKUP APP
        config.add_route(get_lookup_route_name(), get_lookup_route())
        config.add_view(get_lookup_view, route_name=get_lookup_route_name())

        # ======== PORTAL APP
        config.add_route(get_portal_route_name(), get_portal_route())
        config.add_view(get_portal_view, route_name=get_portal_route_name())

        # ======== STATUS APP
        config.add_route(get_status_route_name(), get_status_route())
        config.add_view(get_status_view, route_name=get_status_route_name())

        # ======== FINAL CONFIG
        return config.make_wsgi_app()


def get_server():
    return make_server(get_hostname(), get_port(), get_app())
