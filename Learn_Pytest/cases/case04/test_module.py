# -*- coding: UTF-8 -*-

import pytest
def test_username_02_01(username_02):
    print(">>>>>"*40 + username_02)
    # assert username_02 == "yulikui_01" ->
    assert username_02 == "yulikui_02"


def test_username_02_02(username_02):
    assert username_02 == "yulikui_02"


if __name__ == '__main__':
    pytest.main("-s test_module.py")