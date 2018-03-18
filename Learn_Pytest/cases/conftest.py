# -*- coding: UTF-8 -*-

import pytest
import tempfile
import os



class DBS(object):
    def __init__(self):
        self.intransaction = []
    def begin(self, name):
        self.intransaction.append(name)
    def rollback(self):
        self.intransaction.pop()

@pytest.fixture(scope="module")
def dbs():
    return DBS()