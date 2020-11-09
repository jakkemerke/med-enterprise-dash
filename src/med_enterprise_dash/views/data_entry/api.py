def get_data_entry_organizations(request):
    """This view accepts a query string "s".
    """
    return {}


def get_data_entry_countries(request):
    return []


def get_data_entry_events(request):
    """This view accepts a query string "id".
    """
    return {}


def get_data_entry_traceability(request):
    return {}


def get_data_entry_programs(request):
    return {}


def get_data_entry_tracks(request):
    return {}


def get_data_entry_submission(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_data_entry_terms(request):
    return {}
