# -*- coding: UTF-8 -*-

class TestClass:  
        def test_one(self):  
                assert "h" in "this"  
        def test_two(self):  
                x = "hello"  
                # assert hasattr(x,"check")  ->
                assert hasattr(x,"find")  