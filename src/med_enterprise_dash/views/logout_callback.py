from med_enterprise_dash.config import get_clientside_path_offset, get_branding
from med_enterprise_dash.routes import get_logout_callback_route_name


def get_logout_callback_response():
    return {
        "branding": get_branding(),
        "name": get_logout_callback_route_name(),
        "route_prefix": get_clientside_path_offset(),
    }


def logout_callback(request):
    request.session.invalidate()
    return get_logout_callback_response()
