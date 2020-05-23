def get_lookup_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_lookup_route():
    return "/lookup"


def get_lookup_route_name():
    return "Lookup"


def includeme(config):
    config.add_route(get_lookup_route_name(), get_lookup_route())
    config.add_view(get_lookup_view, route_name=get_lookup_route_name())
