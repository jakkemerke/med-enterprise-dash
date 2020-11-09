def get_data_entry_organizations_route_name():
    return "data_entry_organizations"


def get_data_entry_organizations(request):
    """This view accepts a query string "s".
    """
    return {}


def get_data_entry_countries_route_name():
    return "data_entry_countries"


def get_data_entry_countries(request):
    return [
        {"id": 1, "code": "1", "name": "Cascadia"},
        {"id": 2, "code": "2", "name": "Alaska"},
        {"id": 3, "code": "3", "name": "Siberia"},
        {"id": 4, "code": "4", "name": "Greenland"},
        {"id": 5, "code": "5", "name": "Svalbard"},
    ]


def get_data_entry_events_route_name():
    return "data_entry_events"


def get_data_entry_events(request):
    """This view accepts a query string "id".
    """
    return {}


def get_data_entry_traceability_route_name():
    return "data_entry_traceability"


def get_data_entry_traceability(request):
    return {}


def get_data_entry_programs_route_name():
    return "data_entry_programs"


def get_data_entry_programs(request):
    return {}


def get_data_entry_tracks_route_name():
    return "data_entry_tracks"


def get_data_entry_tracks(request):
    return {}


def get_data_entry_submission_route_name():
    return "data_entry_submission"


def get_data_entry_submission(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_data_entry_terms_route_name():
    return "data_entry_terms"


def get_data_entry_terms(request):
    return {}
