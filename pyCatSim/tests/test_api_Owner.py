#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Owner Class
"""

import pytest

class Cat:
    def __init__(self, name, color="gray"):
        self.name = name
        self.color = color
        self.hunger = 0
        self.mood = 0

    def play(self):
        self.mood += 2
        self.hunger += 1

    def pet(self):
        self.mood += 1

    def status(self):
        return f"{self.name}: Hunger={self.hunger}, Mood={self.mood}"

class Owner:
    def __init__(self, name, cats_owned):
        if not isinstance(cats_owned, (Cat, list)):
            raise TypeError("Must provide Cat or list of Cats")            
        self.name = name
        self.cats_owned = [cats_owned] if isinstance(cats_owned, Cat) else cats_owned
        
        # Validate all are Cat instances
        for cat in self.cats_owned:
            if not isinstance(cat, Cat):
                raise TypeError("All cats must be Cat instances")

    def feed(self, cat):
        if cat not in self.cats_owned:
            raise ValueError("Unowned cat")
        cat.hunger = max(0, cat.hunger - 1)
        cat.mood += 1

    def play_with(self, cat):
        if cat not in self.cats_owned:
            raise ValueError("Unowned cat")
        cat.play()

    def pet(self, cat):
        if cat not in self.cats_owned:
            raise ValueError("Unowned cat")
        cat.pet()

    def list_cats(self):
        return [cat.status() for cat in self.cats_owned]

@pytest.fixture
def sample_cat():
    return Cat(name="Whiskers")

@pytest.fixture
def sample_owner(sample_cat):
    return Owner(name="Alice", cats_owned=sample_cat)

class TesthumanOwnerInit:
    def test_init_t0(self):
        cat1 = Cat(name="Whiskers")
        owner1 = Owner(name="S1", cats_owned=cat1)
        assert owner1.name == 'S1'
        assert isinstance(owner1.cats_owned, list)
        assert len(owner1.cats_owned) == 1

    def test_init_t1(self):
        cat1 = Cat(name="Whiskers")
        cat2 = Cat(name="Boots", color="tabby")
        owner1 = Owner(name="L1", cats_owned=[cat1, cat2])
        assert owner1.name == 'L1'
        assert isinstance(owner1.cats_owned, list)
        assert len(owner1.cats_owned) == 2

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
    sample_owner.feed(sample_cat)
    assert sample_cat.hunger == 4

def test_feed_cat_min_hunger(sample_owner, sample_cat):
    sample_cat.hunger = 0
    sample_owner.feed(sample_cat)
    assert sample_cat.hunger == 0

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
        Owner(name="Dave", cats_owned="Invalid")
