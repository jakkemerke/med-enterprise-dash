from med_enterprise_dash.config import (
    get_clientside_path_offset,
    get_branding,
    get_stewards,
    get_version,
)
from med_enterprise_dash.micro_services.status import (
    get_status_pub_health,
    get_status_pub_integrity,
)
from med_enterprise_dash.routes import get_home_route_name, get_login_route_name
from med_enterprise_dash.utils.footer import get_footer
from med_enterprise_dash.utils.session import get_username


def get_url_to_login(request):
    return request.route_url(get_login_route_name())


def get_home_view(request):
    return {
        "branding": get_branding(),
        "footer": get_footer(),
        "login": get_url_to_login(request),
        "name": get_home_route_name(),
        "route_prefix": get_clientside_path_offset(),
        "status": get_status_pub_health(),
        "status_integrity": get_status_pub_integrity(),
        "stewards": get_stewards(),
        "username": get_username(request),
        "version": get_version(),
    }
