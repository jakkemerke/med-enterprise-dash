# ======== MED =======================================================
def get_route_home_name():
    return "Home"


def get_route_home():
    return "/"


def get_route_apps():
    return "/apps/"


# ======== AUTH ======================================================
def get_api_test_apps_list_route():
    return f"{get_route_apps()}api/test/apps_list"


# ======== APPOINTMENTS ==============================================
def get_api_test_current_user_route():
    return f"{get_route_apps()}api/test/current_user"


def get_api_test_filters_route():
    return f"{get_route_apps()}api/test/filters"


def get_api_test_users_route():
    return f"{get_route_apps()}api/test/users"


def get_api_test_appt_users_route():
    return f"{get_route_apps()}api/test/appt_users"


def get_api_test_appointments_route():
    return f"{get_route_apps()}api/test/appointments"


def get_api_test_reassign_route():
    return f"{get_route_apps()}api/test/reassign"


def get_api_test_take_begin_route():
    return f"{get_route_apps()}api/test/take_begin"


def get_api_test_update_condition_route():
    return f"{get_route_apps()}api/test/update_condition"


def get_api_test_search_route():
    return f"{get_route_apps()}api/test/search"


def get_api_test_add_dropin_route():
    return f"{get_route_apps()}api/test/add_dropin"


def get_api_test_record_route():
    return f"{get_route_apps()}api/test/record"


def get_api_test_add_interaction_route():
    return f"{get_route_apps()}api/test/add_interaction"


def get_api_test_appointment_route():
    return f"{get_route_apps()}api/test/appointment"


def get_api_test_add_message_route():
    return f"{get_route_apps()}api/test/add_message"


def get_api_test_clear_hold_route():
    return f"{get_route_apps()}api/test/clear_hold"


def get_api_test_finish_route():
    return f"{get_route_apps()}api/test/finish"


def get_api_test_reassign_interaction_route():
    return f"{get_route_apps()}api/test/reassign_interaction"


def get_api_test_resolve_interaction_route():
    return f"{get_route_apps()}api/test/resolve_interaction"


# ======== DATA_ENTRY ================================================
def get_data_entry_organizations_route():
    """The view accepts a querystring "s".
    """
    return f"{get_route_apps()}data-entry/organizations"


def get_data_entry_countries_route():
    return f"{get_route_apps()}data-entry/countries"


def get_data_entry_events_route():
    return f"{get_route_apps()}data-entry/events"


def get_data_entry_traceability_route():
    return f"{get_route_apps()}data-entry/traceability"


def get_data_entry_programs_route():
    return f"{get_route_apps()}data-entry/programs"


def get_data_entry_tracks_route():
    return f"{get_route_apps()}data-entry/tracks"


def get_data_entry_submission_route():
    return f"{get_route_apps()}data-entry/submission"


def get_data_entry_terms_route():
    return f"{get_route_apps()}data-entry/terms"
