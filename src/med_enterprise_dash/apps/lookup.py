def get_lookup_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_lookup_route_name():
    return "Lookup"
