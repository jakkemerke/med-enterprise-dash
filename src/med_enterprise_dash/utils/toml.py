# from pathlib import Path
# {Path().home()}/.med_enterprise_dash/config.toml

import toml
from typing import Any, MutableMapping


def get_med_config() -> MutableMapping[str, Any]:
    return toml.load("config.toml")
