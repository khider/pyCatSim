#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Owner Class
"""

''' Tests for pyCatSim.api.human.Owner

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
from pyCatSim import Cat, Owner

class TesthumanOwnerInit:
    ''' Test for Owner instantiation '''
     
    def test_init_t0(self):
         cat1 = Cat(name="Whiskers")
         owner1 = Owner(name="Sasha", cats_owned=cat1)

         assert owner1.name == 'Sasha'
         assert type(owner1.cats_owned) is list
         assert len(owner1.cats_owned) == 1
    
    def test_init_t1(self):
        cat1 = Cat(name="Whiskers")
        cat2 = Cat(name="Boots", color="tabby")
        # Multiple cats
        owner1 = Owner(name="Liam", cats_owned=[cat1, cat2])

        assert owner1.name == 'Liam'
        assert type(owner1.cats_owned) is list
        assert len(owner1.cats_owned) == 2