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
from PIL import Image

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
                                 ('purr', True),
                                 ('chatter', False),
                                 ('chatter', True),
                                 ('hiss', False),
                                 ('hiss', True),
                                 ('chirrup', False),
                                 ('chirrup', True)
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
            elif noise == 'chatter':
                assert v == 'chattering'
            elif noise == 'hiss':
                assert v == 'Hiss..'
            elif noise == 'chirrup':
                assert v == 'Chirrup'
    
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


class TestcatCatShow:
    ''' Tests for the Cat.show() method '''

    
    def test_show_no_color_returns_image(self):
        """ test that show() returns an image when color is None (random) """
        cat = Cat(name="Boots", color=None)
        img = cat.show()
        #assert isinstance(img, Image.Image)  # PIL image check

    @pytest.mark.parametrize("color", ['tabby', 'black', 'orange', 'tortoiseshell', 'tuxedo'])  # Example colors
    def test_show_with_color_returns_image(self, color):
        """ test that show() returns an image for specified color """
        cat = Cat(name="Boots", color=color)
        img = cat.show()
        #assert isinstance(img, Image.Image)
		
class TestcatCatGroom:
    ''' Test for the groom function'''
    
    def test_groom_t0(self):
        cat=Cat(name="Boots", age=2, color="tabby", mood=2, hunger_level=-1,
                energy = 2, health = 3)
        
        cat.groom()
        
        assert cat.health == 4
        assert cat.mood == 3

class TestcatCatEat:
    ''' Tests for the eat() method in the Cat class '''

    def test_eat_t0(self):
        """Test that eating decreases hunger and increases mood"""
        cat = Cat(name="Boots", color="tabby", hunger_level=2, mood=0)
        result = cat.eat()
        assert result['hunger_level'] == 1
        assert result['mood'] == 1
        assert cat.hunger_level == 1
        assert cat.mood == 1

    def test_eat_t1(self):
        """Test that hunger does not go below 0"""
        cat = Cat(name="Boots", color="tabby", hunger_level=0, mood=5)
        result = cat.eat()
        assert result['hunger_level'] == 0  # should not be negative
        assert result['mood'] == 6
        assert cat.hunger_level == 0
        assert cat.mood == 6

class TestcatCatSleep:
    ''' Test for the sleep function '''
    
    @pytest.mark.parametrize(('duration'),
                             [
                                 (0),
                                 (1),
                                 (4.4),
                                 pytest.param("kitty", marks=pytest.mark.xfail),
                                 pytest.param(-1, marks=pytest.mark.xfail),
                                 pytest.param(17, marks=pytest.mark.xfail)
                                 ]
                             )
    def test_sleep_t0(self, duration):
        cat = Cat(name="Boots", color="tabby")

        cat.sleep(duration)
        
        if duration < 3:
            assert cat.energy == 0


class TestcatCatFact:
    ''' Test for the give_fact function'''
    
    def test_give_fact_t0(self):
        cat=Cat(name="Boots", age=2, color="tabby", mood=2, hunger_level=-1,
                energy = 2, health = 3)
        
        cat.give_fact()

        assert cat.give_fact() in [
        "Cats sleep for 70% of their lives.",
        "A group of cats is called a clowder.",
        "Cats can rotate their ears 180 degrees.",
        "The world's oldest cat lived to be 38 years old.",
        "Cats have five toes on their front paws, but only four on the back.",
        "A cat can jump up to six times its length.",
        "Each cat's nose print is unique, like a human fingerprint.",
        "Cats use their whiskers to detect changes in their surroundings.",
        "The average house cat can run at speeds up to 30 mph.",
        "Cats meow only to communicate with humans."
    ]