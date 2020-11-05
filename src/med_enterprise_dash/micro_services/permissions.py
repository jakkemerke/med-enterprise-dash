import json
import ssl
import urllib.request

from requests import post

from med_enterprise_dash.config import get_med_config
from med_enterprise_dash.views.testing_apis import get_api_test_apps_list_payload
from med_enterprise_dash.routes import (
    get_appointments_alternate_route,
    get_appointments_alternate_route_name,
    get_appointments_route,
    get_appointments_route_name,
    get_data_entry_route,
    get_data_entry_route_name,
    get_events_route,
    get_events_route_name,
    get_file_archive_route,
    get_file_archive_route_name,
    get_lookup_route,
    get_lookup_route_name,
    get_portal_route,
    get_portal_route_name,
    get_status_route,
    get_status_route_name,
)


def get_permissions_url(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["url"]


def get_permissions_token(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["token"]


def get_permissions_mode(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["mode"]


def get_permissions_legacy_mode(username):
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    url = get_permissions_url()

    jsondata = json.dumps({"username": username})
    jsondataasbytes = jsondata.encode("utf-8")

    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("token", get_permissions_token())
    req.add_header("Content-Length", len(jsondataasbytes))

    response = urllib.request.urlopen(req, jsondataasbytes, context=myssl)
    return json.loads(response.read().decode("utf-8"))


def get_permissions_standard_mode(username):
    data = {"username": username}
    response = post(get_permissions_url(), data)
    # print(response.status_code)
    # print(response.text)
    return json.loads(response.text)


def get_permissions_testing_mode(username):
    return get_api_test_apps_list_payload()


def get_modes():
    return {
        "testing": get_permissions_testing_mode,
        "legacy": get_permissions_legacy_mode,
        "standard": get_permissions_standard_mode,
    }


def get_permissions_mapping():
    return {
        "appointments": {
            "route": get_appointments_route(),
            "name": get_appointments_route_name(),
        },
        "appointments_lite": {
            "route": get_appointments_alternate_route(),
            "name": get_appointments_alternate_route_name(),
        },
        "data_entry": {
            "route": get_data_entry_route(),
            "name": get_data_entry_route_name(),
        },
        "events": {"route": get_events_route(), "name": get_events_route_name()},
        "file_archive": {
            "route": get_file_archive_route(),
            "name": get_file_archive_route_name(),
        },
        "residents": {"route": get_portal_route(), "name": get_portal_route_name()},
        "search_patients": {
            "route": get_lookup_route(),
            "name": get_lookup_route_name(),
        },
        "system_status": {"route": get_status_route(), "name": get_status_route_name()},
    }


def get_apps_list(permissions_dict):
    apps_list = permissions_dict.get("apps_list", None)
    is_sysadmin = get_sysadmin(permissions_dict)
    apps_routes = []

    for key in get_permissions_mapping():
        if is_sysadmin or apps_list.get(key, False):
            apps_routes.append(get_permissions_mapping().get(key, None))

    return apps_routes


def get_permissions(username):
    return get_modes().get(get_permissions_mode(), get_permissions_standard_mode)(
        username
    )


def get_sysadmin(permissions_dict):
    apps_list = permissions_dict.get("apps_list", None)
    return apps_list["sysadmin"]
