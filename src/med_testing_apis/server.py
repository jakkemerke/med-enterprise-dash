from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response
from pyramid.events import NewRequest

from med_testing_apis.routes import *
from med_testing_apis.views.testing_apis import *
from med_testing_apis.views.data_entry import *
from med_testing_apis.views.status import *


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


def get_home_view(request):
    return Response("OK")


def get_app():
    with Configurator() as config:

        # ======== CORS
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)

        # ======== STATIC HOME ROOT
        config.add_route(get_route_home_name(), get_route_home())
        config.add_view(get_home_view, route_name=get_route_home_name())

        # ======== STATUS ============================================
        # ======== PUB HEALTH
        config.add_route(
            get_status_pub_health_route_name(), get_status_pub_health_route(),
        )
        config.add_view(
            get_status_pub_health,
            route_name=get_status_pub_health_route_name(),
            renderer="json",
        )

        # ======== AUTH ==============================================
        # ======== APPS LIST
        config.add_route(
            get_api_test_apps_list_route_name(), get_api_test_apps_list_route(),
        )
        config.add_view(
            get_api_test_apps_list_view,
            route_name=get_api_test_apps_list_route_name(),
            renderer="json",
        )

        # ======== APPOINTMENTS ======================================
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

        # ======== DATA_ENTRY ========================================

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

        # ======== FINAL CONFIG
        config.add_notfound_view(notfound, append_slash=True)
        return config.make_wsgi_app()


def get_port():
    return 6543


def get_hostname():
    return "localhost"


def get_server():
    return make_server(get_hostname(), get_port(), get_app())
