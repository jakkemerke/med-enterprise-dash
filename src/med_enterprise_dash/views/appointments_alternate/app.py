import pyramid.httpexceptions as exc

from med_enterprise_dash.config import (
    get_branding,
    get_installation_subdirectory,
    get_med_config,
    get_static_path_offset,
)
from med_enterprise_dash.micro_services.permissions import get_apps_routes
from med_enterprise_dash.routes import (
    get_login_route_name,
    get_login_verification_route_name,
)
from med_enterprise_dash.utils.session import get_username
from med_enterprise_dash.views.appointments_alternate.route_names import (
    get_api_test_add_dropin_route_name,
    get_api_test_add_interaction_route_name,
    get_api_test_add_message_route_name,
    get_api_test_appointment_route_name,
    get_api_test_appointments_route_name,
    get_api_test_apps_list_route_name,
    get_api_test_appt_users_route_name,
    get_api_test_clear_hold_route_name,
    get_api_test_current_user_route_name,
    get_api_test_filters_route_name,
    get_api_test_finish_route_name,
    get_api_test_reassign_interaction_route_name,
    get_api_test_reassign_route_name,
    get_api_test_record_route_name,
    get_api_test_resolve_interaction_route_name,
    get_api_test_search_route_name,
    get_api_test_take_begin_route_name,
    get_api_test_update_condition_route_name,
    get_api_test_users_route_name,
    get_appointments_alternate_route_name,
)


def get_clientside_path_offset():
    return get_static_path_offset(get_installation_subdirectory(get_med_config()))


def get_appointments_alternate_view(request):
    if "login_verification" not in request.session:
        request.session["last_stop"] = get_appointments_alternate_route_name()
        raise exc.HTTPFound(request.route_url(get_login_verification_route_name()))

    # request.route_url(  ()),
    if "username" in request.session and "permissions_dict" in request.session:
        return {
            "branding": get_branding(),
            "name": get_appointments_alternate_route_name(),
            "username": get_username(request),
            "route_prefix": get_clientside_path_offset(),
            "apps": get_apps_routes(request.session["permissions_dict"]),
            "apis": {
                "appointments": request.route_url(
                    get_api_test_appointments_route_name()
                ),
                "appt_users": request.route_url(get_api_test_appt_users_route_name()),
                "current_user": request.route_url(
                    get_api_test_current_user_route_name()
                ),
                "filters": request.route_url(get_api_test_filters_route_name()),
                "reassign": request.route_url(get_api_test_reassign_route_name()),
                "takebegin": request.route_url(get_api_test_take_begin_route_name()),
                "update_condition": request.route_url(
                    get_api_test_update_condition_route_name()
                ),
                "users": request.route_url(get_api_test_users_route_name()),
            },
            "external_links": [
                # {"url": "#", "name": "Link1"},
                # {"url": "#", "name": "Link2"},
            ],
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
