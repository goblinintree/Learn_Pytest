# -*- coding: UTF-8 -*-

import pytest

class TestClass(object):
    @pytest.fixture(autouse=True)
    def transacts(self, request, dbs):
        print("transact setup")
        dbs.begin(request.function.__name__)
        yield
        print("transact teardown")
        dbs.rollback()

    def test_method1(self, dbs):
        assert dbs.intransaction == ["test_method1"]

    def test_method2(self, dbs):
        assert dbs.intransaction == ["test_method2"]

        
if __name__ == '__main__':
    pytest.main("-s test_db_transact.py")