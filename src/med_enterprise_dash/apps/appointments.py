def get_appointments_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_appointments_route_name():
    return "Appointments"
