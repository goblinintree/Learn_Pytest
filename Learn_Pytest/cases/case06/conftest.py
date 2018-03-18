# -*- coding: UTF-8 -*-

import pytest
import smtplib

@pytest.fixture(scope="module")
def username_06():
    print(">>>"*40 + "setup") # 
    print("1")
    yield "yulikui_new"  # provide the fixture value
    print(">>>"*40 + "teardown")
    print("2")   
