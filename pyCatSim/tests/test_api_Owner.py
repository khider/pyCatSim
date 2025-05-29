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
        
    # Fixtures
    @pytest.fixture
    def sample_cat():
        return Cat(name="Whiskers")
    
    @pytest.fixture
    def sample_owner(sample_cat):
        return Owner(name="Alice", cats_owned=sample_cat)
    
    # Tests for Cat class
    def test_cat_initialization(sample_cat):
        assert sample_cat.name == "Whiskers"
        assert sample_cat.hunger == 0
        assert sample_cat.mood == 0
    
    def test_cat_play(sample_cat):
        sample_cat.play()
        assert sample_cat.mood == 2
        assert sample_cat.hunger == 1
    
    def test_cat_pet(sample_cat):
        sample_cat.pet()
        assert sample_cat.mood == 1
    
    def test_cat_status(sample_cat):
        sample_cat.hunger = 3
        sample_cat.mood = 5
        assert sample_cat.status() == "Whiskers: Hunger=3, Mood=5"
    
    # Tests for Owner class
    def test_owner_initialization_single_cat(sample_cat):
        owner = Owner(name="Bob", cats_owned=sample_cat)
        assert owner.name == "Bob"
        assert len(owner.cats_owned) == 1
    
    def test_owner_initialization_multiple_cats():
        cats = [Cat(name="Fluffy"), Cat(name="Mittens")]
        owner = Owner(name="Carol", cats_owned=cats)
        assert len(owner.cats_owned) == 2
    
    def test_feed_cat(sample_owner, sample_cat):
        sample_cat.hunger = 5
        sample_cat.mood = 2
        sample_owner.feed(sample_cat)
        assert sample_cat.hunger == 4
        assert sample_cat.mood == 3
    
    def test_feed_cat_min_hunger(sample_owner, sample_cat):
        sample_cat.hunger = 0
        sample_owner.feed(sample_cat)
        assert sample_cat.hunger == 0  # Shouldn't go below 0
    
    def test_feed_unowned_cat(sample_owner):
        stray_cat = Cat(name="Stray")
        with pytest.raises(ValueError):
            sample_owner.feed(stray_cat)
    
    def test_play_with_cat(sample_owner, sample_cat):
        sample_owner.play_with(sample_cat)
        assert sample_cat.mood == 2
        assert sample_cat.hunger == 1
    
    def test_pet_cat(sample_owner, sample_cat):
        sample_owner.pet(sample_cat)
        assert sample_cat.mood == 1
    
    def test_list_cats(sample_owner, sample_cat):
        sample_cat.hunger = 1
        sample_cat.mood = 4
        statuses = sample_owner.list_cats()
        assert statuses == ["Whiskers: Hunger=1, Mood=4"]
    
    def test_invalid_cat_type():
        with pytest.raises(TypeError):
            Owner(name="Dave", cats_owned="This is not a cat")
