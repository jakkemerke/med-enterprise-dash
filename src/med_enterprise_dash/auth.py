from cas import CASClient
from utils import (
    get_cas_client_version,
    get_cas_client_service_url,
    get_cas_client_server_url,
)


def get_auth_client(med_config):
    return CASClient(
        version=get_cas_client_version(med_config),
        service_url=get_cas_client_service_url(med_config),
        server_url=get_cas_client_server_url(med_config),
    )
