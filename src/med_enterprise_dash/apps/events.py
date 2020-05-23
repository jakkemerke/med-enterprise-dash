def get_events_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_events_route_name():
    return "Events"
