from cas import CASClient
from utils import get_host_url, get_profile_route_name


def get_auth_client(med_config):
    return CASClient(
        version=med_config["casclient"]["version"],
        service_url=f"http://{get_host_url()}/login?next={get_profile_route_name()}",
        server_url=med_config["casclient"]["server_url"],
    )
