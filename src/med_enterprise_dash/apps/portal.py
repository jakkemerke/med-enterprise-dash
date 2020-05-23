def get_portal_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_portal_route_name():
    return "Portal"
