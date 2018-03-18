# -*- coding: UTF-8 -*-

import pytest
from conftest import User

def test_username_05_01(user):
    print(">>>>>"*40 + user.username)
    # assert user.username == "yulikui_01" ->
    assert user.username == "yulikui_03"


def test_username_05_02(user):
    assert user.username == "yulikui_03"

if __name__ == '__main__':
    pytest.main("-s test_module_class.py")