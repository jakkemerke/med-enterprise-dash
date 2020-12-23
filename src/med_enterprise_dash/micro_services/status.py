import json
import ssl
import urllib.request

from requests import post, get

from med_enterprise_dash.config import get_med_config


def get_status_url(med_config=get_med_config()):
    return med_config["micro_services"]["status"]["url"]


def get_status_token(med_config=get_med_config()):
    return med_config["micro_services"]["status"]["token"]


def get_status_pub_health_standard_mode():
    response = post(get_status_url())
    return json.loads(response.text)


def get_status_pub_health():
    return get_status_pub_health_standard_mode()
