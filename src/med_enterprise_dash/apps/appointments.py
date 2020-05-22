def get_appointments_view(request):
    from pyramid.response import Response
    return Response('OK')


def get_appointments_route():
    return "/appointments"


def get_appointments_route_name():
    return "Appointments"


def includeme(config):
    config.add_route(get_appointments_route_name(), get_appointments_route())
    config.add_view(get_appointments_view, route_name=get_appointments_route_name())
