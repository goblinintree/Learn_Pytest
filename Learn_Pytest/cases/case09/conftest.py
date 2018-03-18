# -*- coding: UTF-8 -*-

import pytest
import tempfile
import os

@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    print("^^^^^^^^"*5)
    os.chdir(newpath)

# pytestmark = pytest.mark.usefixtures("cleandir")   放这边是不能激活的