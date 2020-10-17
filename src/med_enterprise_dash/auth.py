from cas import CASClient
from config import (
    get_cas_client_server_url,
    get_cas_client_version,
    get_host_url,
    get_installation_subdirectory,
    get_static_path_offset,
)
from routes import get_profile_route_name


def get_cas_client_service_url(med_config):
    return f"{get_host_url(med_config)}/{get_static_path_offset(get_installation_subdirectory(med_config))}login?next={get_profile_route_name()}"


def get_cas_client(med_config):
    return CASClient(
        version=get_cas_client_version(med_config),
        service_url=get_cas_client_service_url(med_config),
        server_url=get_cas_client_server_url(med_config),
    )
