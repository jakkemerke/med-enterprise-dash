import pyramid.httpexceptions as exc

from med_enterprise_dash.config import (
    get_branding,
    get_installation_subdirectory,
    get_med_config,
    get_static_path_offset,
)
from med_enterprise_dash.micro_services.permissions import get_apps_list
from med_enterprise_dash.routes import (
    get_appointments_alternate_route_name,
    get_login_route_name,
    get_login_verification_route_name,
)
from med_enterprise_dash.utils.session import get_username


def get_clientside_path_offset():
    return get_static_path_offset(get_installation_subdirectory(get_med_config()))


def get_appointments_alternate_view(request):
    if "login_verification" not in request.session:
        request.session["last_stop"] = get_appointments_alternate_route_name()
        raise exc.HTTPFound(request.route_url(get_login_verification_route_name()))

    if "username" in request.session and "permissions_dict" in request.session:
        return {
            "branding": get_branding(),
            "name": get_appointments_alternate_route_name(),
            "username": get_username(request),
            "route_prefix": get_clientside_path_offset(),
            "apps": get_apps_list(request.session["permissions_dict"]),
            "apis": {
                "appointments": "http://localhost:6543/apps/api/test/appointments",
                "appt_users": "http://localhost:6543/apps/api/test/appt_users",
                "current_user": "http://localhost:6543/apps/api/test/current_user",
                "filters": "http://localhost:6543/apps/api/test/filters",
                "reassign": "http://localhost:6543/apps/api/test/reassign",
                "takebegin": "http://localhost:6543/apps/api/test/take_begin",
                "update_condition": "http://localhost:6543/apps/api/test/update_condition",
                "users": "http://localhost:6543/apps/api/test/users",
            },
            "external_links": [
                # {"url": "#", "name": "Link1"},
                # {"url": "#", "name": "Link2"},
            ],
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
