from med_enterprise_dash.config import get_clientside_path_offset, get_branding
from med_enterprise_dash.routes import get_home_route_name, get_login_route_name
from med_enterprise_dash.utils.session import get_username


def get_url_to_login(request):
    return request.route_url(get_login_route_name())


def get_home_view(request):
    return {
        "login": get_url_to_login(request),
        "branding": get_branding(),
        "name": get_home_route_name(),
        "username": get_username(request),
        "route_prefix": get_clientside_path_offset(),
    }
