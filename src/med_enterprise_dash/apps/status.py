def get_status_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_status_route_name():
    return "Status"
