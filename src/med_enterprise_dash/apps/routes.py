from apps.appointments import *
from apps.appointments_alternate import *
from apps.data_entry import *
from apps.events import *
from apps.portal import *
from apps.lookup import *
from apps.status import *
from apps.api.test_apis import *


def get_appointments_route():
    return "/appointments"


def get_appointments_alternate_route():
    return "/appointments_alternate"


def get_data_entry_route():
    return "/data_entry"


def get_events_route():
    return "/events"


def get_lookup_route():
    return "/lookup"


def get_portal_route():
    return "/portal"


def get_status_route():
    return "/status"


# def get_api_route():
#     return "/api"


def get_api_test_current_user_route():
    return "/api/test/current_user"


def get_api_test_filters_route():
    return "/api/test/filters"


def get_api_test_users_route():
    return "/api/test/users"


def get_api_test_appt_users_route():
    return "/api/test/appt_users"


def get_api_test_appointments_route():
    return "/api/test/appointments"


def get_api_test_reassign_route():
    return "/api/test/reassign"


def get_api_test_take_begin_route():
    return "/api/test/take_begin"


def get_api_test_update_condition_route():
    return "/api/test/update_condition"


def get_api_test_search_route():
    return "/api/test/search"


def get_api_test_record_route():
    return "/api/test/record"


# TODO: Make this an enabled option via the toml config.
from pyramid.events import NewRequest


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


def includeme(config):
    config.add_route(get_appointments_route_name(), get_appointments_route())
    config.add_view(get_appointments_view, route_name=get_appointments_route_name())

    config.add_route(
        get_appointments_alternate_route_name(), get_appointments_alternate_route()
    )
    config.add_view(
        get_appointments_alternate_view,
        route_name=get_appointments_alternate_route_name(),
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

    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.add_route(
        get_api_test_current_user_route_name(), get_api_test_current_user_route()
    )
    config.add_view(
        get_api_test_current_user_view,
        route_name=get_api_test_current_user_route_name(),
        renderer="json",
    )

    config.add_route(get_api_test_filters_route_name(), get_api_test_filters_route())
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

    config.add_route(get_api_test_reassign_route_name(), get_api_test_reassign_route())
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

    config.add_route(
        get_api_test_search_route_name(), get_api_test_search_route(),
    )
    config.add_view(
        get_api_test_search_view,
        route_name=get_api_test_search_route_name(),
        renderer="json",
    )

    config.add_route(
        get_api_test_record_route_name(), get_api_test_record_route(),
    )
    config.add_view(
        get_api_test_record_view,
        route_name=get_api_test_record_route_name(),
        renderer="json",
    )
