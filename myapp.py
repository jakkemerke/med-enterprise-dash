import os, sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./src")),
)

from wsgiref.simple_server import make_server
from med_enterprise_dash.app import get_server


if __name__ == "__main__":
    server = get_server()
    server.serve_forever()
