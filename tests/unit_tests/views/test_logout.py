import os, sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")),
)

from med_enterprise_dash.views.logout import *


class TestLogout(unittest.TestCase):
    def test_stub(self):
        print(f"stub for {__name__}")
        assert 1 == 1


if __name__ == "__main__":
    print(__name__)
