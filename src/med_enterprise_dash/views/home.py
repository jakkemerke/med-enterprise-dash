from utils.session import get_username
from config import get_clientside_path_offset


from routes import get_home_route_name


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
        "route_prefix": get_clientside_path_offset(),
    }
