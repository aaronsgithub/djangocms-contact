#!/usr/bin/env python
from djangocms_helper import runner

from tests import test_settings


# import settings from test_settings.py file into a dict
HELPER_SETTINGS = {
    setting: getattr(test_settings, setting)
    for setting in dir(test_settings)
    if not setting.startswith("__")
}


def run():
    runner.cms('djangocms_contact')


if __name__ == "__main__":
    run()
