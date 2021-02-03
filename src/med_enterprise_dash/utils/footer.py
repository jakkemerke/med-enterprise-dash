from med_enterprise_dash.config import get_branding, get_stewards, get_version


def get_footer():
    return {
        "branding": get_branding(),
        "stewards": get_stewards(),
        "version": get_version(),
    }
