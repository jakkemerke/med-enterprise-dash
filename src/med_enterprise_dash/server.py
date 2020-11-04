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
from med_enterprise_dash.views.home import get_home_view
from med_enterprise_dash.views.login import login
from med_enterprise_dash.views.logout import logout
from med_enterprise_dash.views.logout_callback import logout_callback
from med_enterprise_dash.views.lookup import get_lookup_view
from med_enterprise_dash.views.portal import get_portal_view
from med_enterprise_dash.views.profile import profile
from med_enterprise_dash.views.status import get_status_view
from med_enterprise_dash.views.test_apis import *


def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update(
            {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST,GET,DELETE,PUT,OPTIONS",
                "Access-Control-Allow-Headers": "Origin, Content-Type, Accept, Authorization",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Max-Age": "1728000",
            }
        )

    event.request.add_response_callback(cors_headers)


def notfound(request):
    return HTTPNotFound()
    # return HTTPTemporaryRedirect()
    # return Response("No Content", status="204 No Content")


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

        # ======== higher level views
        config.add_route(get_home_route_name(), get_route_root())
        config.add_view(
            get_home_view,
            route_name=get_home_route_name(),
            renderer="./templates/home.jinja2",
        )

        config.add_route(get_login_route_name(), get_route_login())
        config.add_view(login, route_name=get_login_route_name())

        config.add_route("logout", get_route_logout())
        config.add_view(logout, route_name="logout")

        config.add_route(get_logout_callback_route_name(), get_route_logout_callback())
        config.add_view(
            logout_callback,
            route_name=get_logout_callback_route_name(),
            renderer="./templates/logout_callback.jinja2",
        )

        config.add_route(get_profile_route_name(), get_route_profile())
        config.add_view(
            profile,
            route_name=get_profile_route_name(),
            renderer="./templates/profile.jinja2",
        )

        config.add_route(get_apps_route_name(), "/apps/")
        config.add_view(
            apps, route_name=get_apps_route_name(), renderer="./templates/apps.jinja2"
        )

        # ======== apps frontends follow.
        config.add_route(get_appointments_route_name(), get_appointments_route())
        config.add_view(get_appointments_view, route_name=get_appointments_route_name())

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
            name=f"appointments_alternate/static/css",
        )
        config.add_static_view(
            path="med_enterprise_dash:static/med-appointments/js",
            name=f"appointments_alternate/static/js",
        )

        config.add_route(get_data_entry_route_name(), get_data_entry_route())
        config.add_view(get_data_entry_view, route_name=get_data_entry_route_name())

        config.add_route(get_events_route_name(), get_events_route())
        config.add_view(get_events_view, route_name=get_events_route_name())

        config.add_route(get_lookup_route_name(), get_lookup_route())
        config.add_view(get_lookup_view, route_name=get_lookup_route_name())

        config.add_route(get_portal_route_name(), get_portal_route())
        config.add_view(get_portal_view, route_name=get_portal_route_name())

        config.add_route(get_status_route_name(), get_status_route())
        config.add_view(get_status_view, route_name=get_status_route_name())

        # ======== CORS and test APIs follow.
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)

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

        # ======== FINAL CONFIG
        # config.include("views.api.routes.includeme", route_prefix=f"{route_prefix}/apps")
        config.add_notfound_view(notfound, append_slash=True)
        return config.make_wsgi_app()


def get_server():
    return make_server(get_hostname(), get_port(), get_app())
