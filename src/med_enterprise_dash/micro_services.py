import json
import ssl
import urllib.request

from med_config import get_med_config


def get_permissions_url(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["url"]


def get_permissions_token(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["token"]


def get_user_roles(permissions):
    return permissions["auth"]["user"]["global"][0]


def get_permissions_map_sysadmin(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["sysadmin"]


def get_permissions_map_appointments(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["appointments"]


def get_permissions_map_appointments_lite(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["appointments_lite"]


def get_permissions_map_data_entry(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["data_entry"]


def get_permissions_map_events(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["events"]


def get_permissions_map_file_archive(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["file_archive"]


def get_permissions_map_residents(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["residents"]


def get_permissions_map_search_patients(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["search_patients"]


def get_permissions_map_system_status(med_config=get_med_config()):
    return med_config["micro_services"]["permissions"]["map"]["system_status"]


def has_role_sysadmin(user_roles):
    return 1 == user_roles[get_permissions_map_sysadmin()]


def has_role_appointments(user_roles):
    return 1 == user_roles[get_permissions_map_appointments()]


def has_role_appointments_lite(user_roles):
    return 1 == user_roles[get_permissions_map_appointments_lite()]


def has_role_data_entry(user_roles):
    return 1 == user_roles[get_permissions_map_data_entry()]


def has_role_events(user_roles):
    return 1 == user_roles[get_permissions_map_events()]


def has_role_file_archive(user_roles):
    return 1 == user_roles[get_permissions_map_file_archive()]


def has_role_residents(user_roles):
    return 1 == user_roles[get_permissions_map_residents()]


def has_role_search_patients(user_roles):
    return 1 == user_roles[get_permissions_map_search_patients()]


def has_role_system_status(user_roles):
    return 1 == user_roles[get_permissions_map_system_status()]


def get_permissions(username):
    # NOTE: This one works, but some other endpoints such as ASP.NET
    # hacks don't work here.
    # import requests
    # data = {'title':'Python Requests','body':'Requests are awesome','userId':1}
    # response = requests.post('https://jsonplaceholder.typicode.com/posts', data)
    # print(response.status_code)
    # print(response.text)

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


def get_apps_list(username):
    user_roles = get_user_roles(get_permissions(username))
    is_sysadmin = has_role_sysadmin(user_roles)

    apps_routes = []
    # TODO: Also add each role to the session.
    if is_sysadmin or has_role_appointments(user_roles):
        apps_routes.append({"route": "#", "name": "Appointments"})
    if is_sysadmin or has_role_appointments_lite(user_roles):
        apps_routes.append({"route": "#", "name": "AppointmentsLite"})
    if is_sysadmin or has_role_data_entry(user_roles):
        apps_routes.append({"route": "#", "name": "DataEntry"})
    if is_sysadmin or has_role_events(user_roles):
        apps_routes.append({"route": "#", "name": "Events"})
    if is_sysadmin or has_role_file_archive(user_roles):
        apps_routes.append({"route": "#", "name": "FileArchive"})
    if is_sysadmin or has_role_residents(user_roles):
        apps_routes.append({"route": "#", "name": "Residents"})
    if is_sysadmin or has_role_search_patients(user_roles):
        apps_routes.append({"route": "#", "name": "SearchPatients"})
    if is_sysadmin or has_role_system_status(user_roles):
        apps_routes.append({"route": "#", "name": "SystemStatus"})

    return apps_routes
