# from pathlib import Path
# {Path().home()}/.med_enterprise_dash/config.toml

import toml


def get_med_config():
    return toml.load("config.toml")
