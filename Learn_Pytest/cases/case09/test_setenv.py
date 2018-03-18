# -*- coding: UTF-8 -*-

import os
import pytest

pytestmark = pytest.mark.usefixtures("cleandir") 

class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile.txt", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        print("__" * 40 + os.getcwd() )
        assert os.listdir(os.getcwd()) == []

if __name__ == '__main__':
    pytest.main("-s test_setenv.py")