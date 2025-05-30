#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The human module controls the behavior of humans around cats
"""
from pyCatSim.api.cat import Cat

class Owner:
    """
    Represents a cat owner who can care for one or more cats.

    Parameters
    ----------
    name : str
        The name of the owner.
    cats_owned : Cat or list of Cat
        A single Cat instance or a list of Cat instances representing the cats this owner is responsible for.

    Attributes
    ----------
    name : str
        The name of the owner.
    cats_owned : list of Cat
        The list of Cat objects owned by this person.

    Raises
    ------
    TypeError
        If cats_owned is neither a Cat nor a list of Cat objects.

    Examples
    --------
    .. jupyter-execute::
    
        from pyCatSim import Cat, Owner

        cat1 = Cat(name="Whiskers")
        cat2 = Cat(name="Boots", color="tabby")

        # Single cat
        owner1 = Owner(name="Sasha", cats_owned=cat1)

        # Multiple cats
        owner2 = Owner(name="Liam", cats_owned=[cat1, cat2])

        print(owner1.name)
        print([cat.name for cat in owner2.cats_owned])

    """
    def __init__(self, name, cats_owned):
        if isinstance(cats_owned, Cat):
            cats_owned = [cats_owned]
        elif isinstance(cats_owned, list):
            if not all(isinstance(cat, Cat) for cat in cats_owned):
                raise TypeError("All elements in cats_owned must be instances of Cat.")
        else:
            raise TypeError("cats_owned must be a Cat instance or a list of Cat instances.")

        self.name = name
        self.cats_owned = cats_owned

    def feed(self, cat):
        """
        Feed the specified cat owned by this Owner.

        Parameters
        ----------
        cat : Cat
            The cat to feed. Must be owned by this owner.

        Raises
        ------
        ValueError
            If the specified cat is not owned by this owner.
        AttributeError
            If the cat does not have 'hunger_level' or 'mood' attributes.
        """
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        if not hasattr(cat, 'hunger_level') or not hasattr(cat, 'mood'):
            raise AttributeError("Cat must have 'hunger_level' and 'mood' attributes.")

        cat.hunger_level = max(0, cat.hunger_level - 1)
        cat.mood += 1

    def play_with(self, cat):
        """
        Play with the specified cat owned by this Owner.
        """
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        cat.play()

    def pet(self, cat):
        """
        Pet the specified cat owned by this Owner.
        """
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        cat.pet()

    def list_cats(self):
        """
        Return a list of status strings for all owned cats.

        Returns
        -------
        list of str
            List of status strings for each owned cat.
        """
        return [cat.status() for cat in self.cats_owned]
    
    def give_fact(self):
        """Give a cat fact."""
        print("Cats are amazing!")

    def adopt(self, new_cats):
        """Adopt one or more new cats."""
        if isinstance(new_cats, list):
            self.cats_owned.extend(new_cats)
        else:
            self.cats_owned.append(new_cats)

    def groom(self, cat):
        """Groom a cat, increasing its mood."""
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        cat.mood += 1