from routes.utils import (
    get_home_route_name,
    get_username,
)


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
    }
