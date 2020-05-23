def get_portal_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_portal_route():
    return "/portal"


def get_portal_route_name():
    return "Portal"


def includeme(config):
    config.add_route(get_portal_route_name(), get_portal_route())
    config.add_view(get_portal_view, route_name=get_portal_route_name())
