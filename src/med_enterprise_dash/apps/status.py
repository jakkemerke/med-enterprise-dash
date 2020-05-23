def get_status_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_status_route():
    return "/status"


def get_status_route_name():
    return "Status"


def includeme(config):
    config.add_route(get_status_route_name(), get_status_route())
    config.add_view(get_status_view, route_name=get_status_route_name())
