from med_enterprise_dash.utils.toml import get_med_config
from med_enterprise_dash.config import (
    get_route_prefix,
    get_installation_subdirectory,
)


def get_route_subdir():
    med_config = get_med_config()
    subdirectory = get_installation_subdirectory(med_config)
    return get_route_prefix(subdirectory)


# ======== MED =======================================================
def get_home_route_name():
    return "Home"


def get_route_root():
    return f"{get_route_subdir()}/"


def get_login_route_name():
    return "Login"


def get_route_login():
    return f"{get_route_root()}login/"


def get_login_verification_route_name():
    return "login_verification"


def get_route_login_verification():
    return f"{get_route_root()}login/verification"


def get_logout_route_name():
    return "logout"


def get_route_logout():
    return f"{get_route_root()}logout/"


def get_logout_callback_route_name():
    return "logout_callback"


def get_route_logout_callback():
    return f"{get_route_root()}logout_callback/"


def get_profile_route_name():
    return "Profile"


def get_route_profile():
    return f"{get_route_root()}profile/"


def get_apps_route_name():
    return "Apps"


def get_route_apps():
    return f"{get_route_root()}apps/"


# ======== APPS ======================================================
def get_appointments_route_name():
    return "Appointments"


def get_appointments_route():
    return f"{get_route_apps()}appointments"


def get_appointments_alternate_route():
    return f"{get_route_apps()}appointments_alternate"


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


# ======== APPOINTMENTS API ==========================================
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


# ======== DATA_ENTRY API ============================================


def get_data_entry_organizations_route():
    return f"{get_data_entry_route()}/organizations"


def get_data_entry_countries_route():
    return f"{get_data_entry_route()}/countries"


def get_data_entry_events_route():
    return f"{get_data_entry_route()}/events"


def get_data_entry_traceability_route():
    return f"{get_data_entry_route()}/traceability-tags"


def get_data_entry_programs_route():
    return f"{get_data_entry_route()}/programs"


def get_data_entry_tracks_route():
    return f"{get_data_entry_route()}/tracks"


def get_data_entry_submission_route():
    return f"{get_data_entry_route()}/submission"


def get_data_entry_terms_route():
    return f"{get_data_entry_route()}/terms"
