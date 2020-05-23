def get_appointments_alternate_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_appointments_alternate_route_name():
    return "Appointments_Alternate"
