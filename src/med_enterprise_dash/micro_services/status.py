import json
import ssl
import urllib.request

from requests import post

from med_enterprise_dash.config import get_med_config


def get_status_url(med_config=get_med_config()):
    return med_config["micro_services"]["status"]["url"]


def get_status_url_integrity(med_config=get_med_config()):
    return med_config["micro_services"]["status"]["url_integrity"]


def get_status_token(med_config=get_med_config()):
    return med_config["micro_services"]["status"]["token"]


def get_status_pub_health():
    try:
        response = post(get_status_url())
        return json.loads(response.text)
    except:
        # TODO: log this
        return None


# TODO: log the bad
def get_status_pub_integrity() -> str:
    try:
        response = post(get_status_url_integrity())
        if json.loads(response.text) == "0":
            return "PASS"
        else:
            return "DEGRADED"
    except:
        return "CRITITAL"
