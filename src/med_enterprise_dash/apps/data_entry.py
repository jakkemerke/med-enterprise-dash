def get_data_entry_view(request):
    from pyramid.response import Response

    return Response("OK")


def get_data_entry_route_name():
    return "Data_Entry"
