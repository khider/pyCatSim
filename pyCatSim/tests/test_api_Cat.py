#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Cat Class
"""

''' Tests for pyCatSim.api.cat.Cat

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
from pyCatSim import Cat

class TestcatCatInit:
    ''' Test for Cat instantiation '''
     
    def test_init_t0(self):
         cat = Cat(name="Boots", color="tabby")
         assert cat.name == 'Boots'
         assert cat.color == 'tabby'
    
    def test_init_t1(self):
        cat=Cat(name="Boots", age=2, color="tabby", mood=2, hunger_level=-1,
                energy = 2, health = 3)
        assert cat.name == 'Boots'
        assert cat.color == 'tabby'
        assert cat.age == 2
        assert cat.mood == 2
        assert cat.hunger_level == -1
        assert cat.energy == 2
        assert cat.health == 3

class TestcatCatNoise:
    ''' Test for Cat noise'''
    @pytest.mark.parametrize(('noise','play'),
                             [
                                 ('meow', False),
                                 ('meow', True),
                                 ('purr', False),
                                 ('purr', True)
                            ]
                            )
    def test_noise_t0(self,noise,play):
        if sys.platform == "linux" and play is True:
            pytest.skip("Skipping sound playback test on Linux.")

        cat = Cat(name="Boots", color="tabby")
        if play is True:
            cat.make_noise(noise,play)
        else:
            v = cat.make_noise(noise,play)
            if noise == 'meow':
                assert v == 'Meow!'
            elif noise == 'purr':
                assert v == 'Purrr'
    
    
    @pytest.mark.xfail
    def test_noise_t1(self, noise='speak'):
        cat = Cat(name="Boots", color="tabby")
        cat.make_noise()

class TestcatCatPlay:
    ''' Test for the play function'''
    
    def test_play_t0(self):
        cat=Cat(name="Boots", age=2, color="tabby", mood=2, hunger_level=-1,
                energy = 2, health = 3)
        
        cat.play()
        
        assert cat.mood == 3
        assert cat.hunger_level == 0
        assert cat.energy == 1

class TestcatCatBathe:
    ''' Test for the bathe function '''

    def test_bathe_t0(self):
        cat = Cat(name="Boots", mood=2, health=4)
        cat.bathe()
        assert cat.mood == 1
        assert cat.health == 5
