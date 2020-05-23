def get_data_entry_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_data_entry_route():
    return "/data_entry"


def get_data_entry_route_name():
    return "Data_Entry"


def includeme(config):
    config.add_route(get_data_entry_route_name(), get_data_entry_route())
    config.add_view(get_data_entry_view, route_name=get_data_entry_route_name())
