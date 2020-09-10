from pyramid.response import Response
import pyramid.httpexceptions as exc

from utils import (
    # get_apps_route_name,
    # get_home_route_name,
    get_installation_subdirectory,
    # get_login_route_name,
    # get_logout_callback_route_name,
    get_med_config,
    # get_profile_route_name,
    get_static_path_offset,
    get_username,
    # is_logged_in,
)
from micro_services import get_apps_list


def get_clientside_path_offset():
    return get_static_path_offset(get_installation_subdirectory(get_med_config()))


def get_appointments_alternate_view(request):
    # from pyramid.response import Response

    # return Response("OK")
    # session = request.session
    # if "username" in session:
    #     return {
    #         "name": get_profile_route_name(),
    #         "username": get_username(request),
    #         "route_prefix": get_clientside_path_offset(),
    #         "apps": get_apps_list(get_username(request)),
    #         "external_links": [
    #             # {"url": "#", "name": "Link1"},
    #             # {"url": "#", "name": "Link2"},
    #         ],
    #     }
    # else:
    #     raise exc.HTTPFound(request.route_url(get_login_route_name()))
    return {
        "name": "testing",
        "username": "foo",
        "route_prefix": get_clientside_path_offset(),
        "apps": get_apps_list(get_username(request)),
        "external_links": [
            # {"url": "#", "name": "Link1"},
            # {"url": "#", "name": "Link2"},
        ],
    }


def get_appointments_alternate_route_name():
    return "Appointments_Alternate"
