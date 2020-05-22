def get_appointments_alternate_view(request):
    from pyramid.response import Response
    return Response('OK')


def get_appointments_alternate_route():
    return "/appointments_alternate"


def get_appointments_alternate_route_name():
    return "Appointments_Alternate"


def includeme(config):
    config.add_route(get_appointments_alternate_route_name(), get_appointments_alternate_route())
    config.add_view(get_appointments_alternate_view, route_name=get_appointments_alternate_route_name())
