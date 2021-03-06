# -*- coding: UTF-8 -*-

import os
import pytest

@pytest.mark.usefixtures("cleandir") 
class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

        
if __name__ == '__main__':
    pytest.main("-s test_setenv.py")