def get_events_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_events_route():
    return "/events"


def get_events_route_name():
    return "Events"


def includeme(config):
    config.add_route(get_events_route_name(), get_events_route())
    config.add_view(get_events_view, route_name=get_events_route_name())
