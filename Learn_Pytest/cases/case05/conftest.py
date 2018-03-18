# -*- coding: UTF-8 -*-

import pytest
import smtplib

class User(object):
    def __init__(self, username):
        self.username = username
    pass

@pytest.fixture(scope="module")
def user():
    user = User("yulikui_03")
    return user
