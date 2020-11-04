from med_enterprise_dash.config import get_clientside_path_offset
from med_enterprise_dash.routes import get_home_route_name
from med_enterprise_dash.utils.session import get_username


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
        "route_prefix": get_clientside_path_offset(),
    }
