from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory, JSONSerializer
from pyramid.httpexceptions import HTTPNotFound

# TODO: Make this an enabled option via the toml config.
from pyramid.events import NewRequest

from med_enterprise_dash.config import (
    get_port,
    get_hostname,
    get_installation_subdirectory,
    get_static_path_offset,
)
from med_enterprise_dash.routes import *
from med_enterprise_dash.utils.toml import get_med_config
from med_enterprise_dash.views.appointments import get_appointments_view
from med_enterprise_dash.views.appointments_alternate.app import (
    get_appointments_alternate_view,
)
from med_enterprise_dash.views.appointments_alternate.api import *
from med_enterprise_dash.views.appointments_alternate.route_names import *
from med_enterprise_dash.views.apps import apps
from med_enterprise_dash.views.data_entry.api import *
from med_enterprise_dash.views.data_entry.app import get_data_entry_view
from med_enterprise_dash.views.data_entry.route_names import *
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

        # ======== APPOINTMENTS_ALTERNATE APP ========
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

        # ======== APPOINTMENTS_ALTERNATE APIs

        # ======== APPOINTMENTS, GENERAL, ETC
        config.add_route(
            get_api_test_current_user_route_name(), get_api_test_current_user_route()
        )
        config.add_view(
            get_api_test_current_user_view,
            route_name=get_api_test_current_user_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_filters_route_name(), get_api_test_filters_route()
        )
        config.add_view(
            get_api_test_filters_view,
            route_name=get_api_test_filters_route_name(),
            renderer="json",
        )

        config.add_route(get_api_test_users_route_name(), get_api_test_users_route())
        config.add_view(
            get_api_test_users_view,
            route_name=get_api_test_users_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_appt_users_route_name(), get_api_test_appt_users_route()
        )
        config.add_view(
            get_api_test_appt_users_view,
            route_name=get_api_test_appt_users_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_appointments_route_name(), get_api_test_appointments_route()
        )
        config.add_view(
            get_api_test_appointments_view,
            route_name=get_api_test_appointments_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_reassign_route_name(), get_api_test_reassign_route()
        )
        config.add_view(
            get_api_test_reassign_view,
            route_name=get_api_test_reassign_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_take_begin_route_name(), get_api_test_take_begin_route()
        )
        config.add_view(
            get_api_test_take_begin_view,
            route_name=get_api_test_take_begin_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_update_condition_route_name(),
            get_api_test_update_condition_route(),
        )
        config.add_view(
            get_api_test_update_condition_view,
            route_name=get_api_test_update_condition_route_name(),
            renderer="json",
        )

        # ======== SEARCH
        config.add_route(
            get_api_test_search_route_name(), get_api_test_search_route(),
        )
        config.add_view(
            get_api_test_search_view,
            route_name=get_api_test_search_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_add_dropin_route_name(), get_api_test_add_dropin_route(),
        )
        config.add_view(
            get_api_test_add_dropin_view,
            route_name=get_api_test_add_dropin_route_name(),
            renderer="json",
        )

        # ======== RECORD aka CONTACT
        config.add_route(
            get_api_test_record_route_name(), get_api_test_record_route(),
        )
        config.add_view(
            get_api_test_record_view,
            route_name=get_api_test_record_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_add_interaction_route_name(),
            get_api_test_add_interaction_route(),
        )
        config.add_view(
            get_api_test_add_interaction_view,
            route_name=get_api_test_add_interaction_route_name(),
            renderer="json",
        )

        # ======== APPOINTMENT aka INTERACTION aka CASE
        config.add_route(
            get_api_test_appointment_route_name(), get_api_test_appointment_route(),
        )
        config.add_view(
            get_api_test_appointment_view,
            route_name=get_api_test_appointment_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_add_message_route_name(), get_api_test_add_message_route(),
        )
        config.add_view(
            get_api_test_add_message_view,
            route_name=get_api_test_add_message_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_clear_hold_route_name(), get_api_test_clear_hold_route(),
        )
        config.add_view(
            get_api_test_clear_hold_view,
            route_name=get_api_test_clear_hold_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_finish_route_name(), get_api_test_finish_route(),
        )
        config.add_view(
            get_api_test_finish_view,
            route_name=get_api_test_finish_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_reassign_interaction_route_name(),
            get_api_test_reassign_interaction_route(),
        )
        config.add_view(
            get_api_test_reassign_interaction_view,
            route_name=get_api_test_reassign_interaction_route_name(),
            renderer="json",
        )

        config.add_route(
            get_api_test_resolve_interaction_route_name(),
            get_api_test_resolve_interaction_route(),
        )
        config.add_view(
            get_api_test_resolve_interaction_view,
            route_name=get_api_test_resolve_interaction_route_name(),
            renderer="json",
        )

        # ======== DATA_ENTRY APP ========
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

        # ======== DATA_ENTRY APIs
        # get_data_entry_organizations
        config.add_route(
            get_data_entry_organizations_route_name(),
            get_data_entry_organizations_route(),
        )
        config.add_view(
            get_data_entry_organizations,
            route_name=get_data_entry_organizations_route_name(),
            renderer="json",
        )

        # get_data_entry_countries
        config.add_route(
            get_data_entry_countries_route_name(), get_data_entry_countries_route(),
        )
        config.add_view(
            get_data_entry_countries,
            route_name=get_data_entry_countries_route_name(),
            renderer="json",
        )

        # get_data_entry_events
        config.add_route(
            get_data_entry_events_route_name(), get_data_entry_events_route(),
        )
        config.add_view(
            get_data_entry_events,
            route_name=get_data_entry_events_route_name(),
            renderer="json",
        )

        # get_data_entry_traceability
        config.add_route(
            get_data_entry_traceability_route_name(),
            get_data_entry_traceability_route(),
        )
        config.add_view(
            get_data_entry_traceability,
            route_name=get_data_entry_traceability_route_name(),
            renderer="json",
        )

        # get_data_entry_programs
        config.add_route(
            get_data_entry_programs_route_name(), get_data_entry_programs_route(),
        )
        config.add_view(
            get_data_entry_programs,
            route_name=get_data_entry_programs_route_name(),
            renderer="json",
        )

        # get_data_entry_tracks
        config.add_route(
            get_data_entry_tracks_route_name(), get_data_entry_tracks_route(),
        )
        config.add_view(
            get_data_entry_tracks,
            route_name=get_data_entry_tracks_route_name(),
            renderer="json",
        )

        # get_data_entry_submission
        config.add_route(
            get_data_entry_submission_route_name(), get_data_entry_submission_route(),
        )
        config.add_view(
            get_data_entry_submission,
            route_name=get_data_entry_submission_route_name(),
            renderer="json",
        )

        # get_data_entry_terms
        config.add_route(
            get_data_entry_terms_route_name(), get_data_entry_terms_route(),
        )
        config.add_view(
            get_data_entry_terms,
            route_name=get_data_entry_terms_route_name(),
            renderer="json",
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
