import pyramid.httpexceptions as exc


from med_enterprise_dash.config import get_clientside_path_offset, get_branding
from med_enterprise_dash.routes import get_login_route_name, get_apps_route_name
from med_enterprise_dash.utils.session import get_username


def get_apps_response(request):
    return {
        "branding": get_branding(),
        "name": get_apps_route_name(),
        "username": get_username(request),
        "route_prefix": get_clientside_path_offset(),
    }


def apps(request):
    session = request.session
    if "username" in session:
        return get_apps_response(request)
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
