from med_enterprise_dash.utils.toml import get_med_config

# TODO: Either get this from the pyproject, or add it to the config.
def get_version():
    return "0.1.1"


def get_port(med_config=get_med_config()):
    return med_config["port"]


def get_hostname(med_config=get_med_config()):
    return med_config["host"]


def get_scheme(med_config=get_med_config()):
    return med_config["scheme"]


def get_home_url_port(port):
    return "" if port == "" else f":{port}"


def get_home_url_scheme(scheme):
    return "" if scheme == "" else f"{scheme}://"


def get_host_url(med_config):
    return f"{get_home_url_scheme(get_scheme(med_config))}{get_hostname()}{get_home_url_port(get_port(med_config))}"


def get_installation_subdirectory(med_config):
    return med_config["subdirectory"]


def get_route_prefix(subdirectory):
    return "" if subdirectory == "" else f"/{subdirectory}"


def get_static_path_offset(subdirectory):
    return "" if subdirectory == "" else f"{subdirectory}/"


def get_cas_client_version(med_config):
    return med_config["casclient"]["version"]


def get_cas_client_server_url(med_config):
    return med_config["casclient"]["server_url"]


def get_clientside_path_offset():
    return get_static_path_offset(get_installation_subdirectory(get_med_config()))


def developer_auto_login_enabled(med_config=get_med_config()):
    return med_config["developer"]["auto_login"]


def get_developer_username(med_config=get_med_config()):
    return med_config["developer"]["username"]


def get_branding(med_config=get_med_config()):
    return med_config["branding"]


def get_stewards(med_config=get_med_config()):
    return med_config["stewards"]
