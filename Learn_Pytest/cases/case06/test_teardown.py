# -*- coding: UTF-8 -*-

import pytest
def test_username_06_01(username_06):
    print(">>>>>"*40 + username_06)
    # assert username_06 == "yulikui_old" ->
    assert username_06 == "yulikui_new"


def test_username_06_02(username_06):
    print(">>>>>"*40 + username_06)
    assert username_06 == "yulikui_new"


if __name__ == '__main__':
    pytest.main("-s test_teardown.py")