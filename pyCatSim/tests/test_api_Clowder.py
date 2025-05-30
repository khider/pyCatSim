#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Clowder Class
"""

''' Tests for pyCatSim.api.cat.Clowder

Naming rules:
1. class: Test{filename}{Class}{method} with appropriate camel case
2. function: test_{method}_t{test_id}
Notes on how to test:
0. Make sure [pytest](https://docs.pytest.org) has been installed: `pip install pytest`
1. execute `pytest {directory_path}` in terminal to perform all tests in all testing files inside the specified directory
2. execute `pytest {file_path}` in terminal to perform all tests in the specified file
3. execute `pytest {file_path}::{TestClass}::{test_method}` in terminal to perform a specific test class/method inside the specified file
4. after `pip install pytest-xdist`, one may execute "pytest -n 4" to test in parallel with number of workers specified by `-n`
5. for more details, see https://docs.pytest.org/en/stable/usage.html
'''

import pytest
import sys
from pyCatSim import Cat,Clowder

class TestcatClowderInit:
    ''' Test for Clowder instantiation '''

    def test_init_t0(self):
        c = Clowder()
        assert c.catlist == []

    def test_init_t1(self):
        cat1 = Cat(name="A")
        cat2 = Cat(name="B")
        c = Clowder([cat1, cat2])
        assert cat1 in c.catlist and cat2 in c.catlist

    @pytest.mark.xfail
    def test_init_t2(self):
        Clowder(["not_a_cat"])  

class TestcatClowderAdd:
    ''' Test for Clowder add_cat '''

    def test_add_cat_t0(self):
        c = Clowder()
        cat = Cat(name="Boots")
        c.add_cat(cat)
        assert cat in c.catlist

    @pytest.mark.xfail
    def test_add_cat_t1(self):
        c = Clowder()
        c.add_cat("not_a_cat")  # should raise TypeError

class TestcatClowderRemove:
    ''' Test for Clowder remove_cat '''
    def test_remove_cat_t0(self):
        cat = Cat(name="Boots")
        c = Clowder([cat])
        c.remove_cat(cat)
        assert cat not in c.catlist

    @pytest.mark.xfail
    def test_remove_cat_t1(self):
        cat1 = Cat(name="Boots")
        cat2 = Cat(name="Shadow")
        c = Clowder([cat1])
        c.remove_cat(cat2)  # should raise ValueError