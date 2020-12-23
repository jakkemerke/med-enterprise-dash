from med_enterprise_dash.config import (
    get_clientside_path_offset,
    get_branding,
    get_stewards,
)
from med_enterprise_dash.micro_services.status import get_status_pub_health
from med_enterprise_dash.routes import get_home_route_name, get_login_route_name
from med_enterprise_dash.utils.session import get_username
from med_enterprise_dash import __version__


def get_url_to_login(request):
    return request.route_url(get_login_route_name())


def get_home_view(request):
    return {
        "branding": get_branding(),
        "login": get_url_to_login(request),
        "name": get_home_route_name(),
        "route_prefix": get_clientside_path_offset(),
        "status": get_status_pub_health(),
        "stewards": get_stewards(),
        "username": get_username(request),
        "version": __version__,
    }
