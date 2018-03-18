# -*- coding: UTF-8 -*-
import pytest

@pytest.fixture
def username_01():
    return "yulikui_01"

def test_username_01_01(username_01):
    assert username_01 == "yulikui_01"
def test_username_01_02(username_01):
    # assert username_01 == "yulikui" ->
    assert username_01 == "yulikui_01"

if __name__ == '__main__':
    pytest.main("-s test_smtpsimple.py")
