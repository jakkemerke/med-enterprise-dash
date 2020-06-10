from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import os, sys

if "med_enterprise_dash" not in sys.path:
    sys.path.insert(0, os.path.abspath("./src/med_enterprise_dash/"))


def hello_world(request):
    return Response(f"Hello from fastcgi and python from iis!!! {sys.path}")


def get_app():
    from med_enterprise_dash import get_app as get_app_med

    return get_app_med()


if __name__ == "__main__":
    server = make_server("0.0.0.0", 6543, get_app())
    server.serve_forever()
