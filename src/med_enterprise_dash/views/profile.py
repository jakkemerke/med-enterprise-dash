import pyramid.httpexceptions as exc

from med_enterprise_dash.config import get_clientside_path_offset
from med_enterprise_dash.micro_services import get_apps_list
from med_enterprise_dash.routes import get_login_route_name, get_profile_route_name
from med_enterprise_dash.utils.session import get_username


def get_url_to_login(request):
    return request.route_url(get_login_route_name())


def get_profile_response(request):
    return {
        "name": get_profile_route_name(),
        "username": get_username(request),
        "route_prefix": get_clientside_path_offset(),
        "apps": get_apps_list(get_username(request)),
        "external_links": [
            # {"url": "#", "name": "Link1"},
            # {"url": "#", "name": "Link2"},
        ],
    }


def profile(request):
    session = dict() if not hasattr(request, "session") else request.session
    if "username" in session:
        return get_profile_response(request)
    else:
        raise exc.HTTPFound(get_url_to_login(request))
