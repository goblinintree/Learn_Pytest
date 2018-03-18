# -*- coding: UTF-8 -*-

import pytest
import smtplib

@pytest.fixture(scope="module")
def username_02():
    return "yulikui_02"
