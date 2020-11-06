# ======== MED =======================================================
def get_home_route_name():
    return "Home"


def get_route_root():
    return "/"


def get_login_route_name():
    return "Login"


def get_route_login():
    return "/login/"


def get_login_verification_route_name():
    return "login_verification"


def get_route_login_verification():
    return "/login/verification"


def get_logout_route_name():
    return "logout"


def get_route_logout():
    return "/logout/"


def get_logout_callback_route_name():
    return "logout_callback"


def get_route_logout_callback():
    return "/logout_callback/"


def get_profile_route_name():
    return "Profile"


def get_route_profile():
    return "/profile/"


def get_apps_route_name():
    return "Apps"


def get_route_apps():
    return "/apps/"


# ======== APPS ======================================================
def get_appointments_route_name():
    return "Appointments"


def get_appointments_route():
    return f"{get_route_apps()}appointments"


def get_appointments_alternate_route_name():
    return "Appointments_Alternate"


def get_appointments_alternate_route():
    return f"{get_route_apps()}appointments_alternate"


def get_data_entry_route_name():
    return "Data_Entry"


def get_data_entry_route():
    return f"{get_route_apps()}data_entry"


def get_events_route_name():
    return "Events"


def get_events_route():
    return f"{get_route_apps()}events"


def get_file_archive_route_name():
    return "File_Archive"


def get_file_archive_route():
    return f"{get_route_apps()}file_archive"


def get_lookup_route_name():
    return "Lookup"


def get_lookup_route():
    return f"{get_route_apps()}lookup"


def get_portal_route_name():
    return "Portal"


def get_portal_route():
    return f"{get_route_apps()}portal"


def get_status_route_name():
    return "Status"


def get_status_route():
    return f"{get_route_apps()}status"
