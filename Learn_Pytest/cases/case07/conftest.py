# -*- coding: UTF-8 -*-

import pytest
import smtplib

class User(object):
    def __init__(self, username):
        self.username = username
    
    def clear_name(self):
        self.username =""
        pass
    pass

@pytest.fixture(scope="module")
def user():
    user = User("yulikui_03")
    return user

@pytest.fixture(scope="module")
def user_addfinalizer(request):
    user = User("yulikui_03")
    def fin():
        print ("teardown smtp")
        user.clear_name()
    request.addfinalizer(fin)
    return user  # provide the fixture value