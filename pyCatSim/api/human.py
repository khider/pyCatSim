#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The human module controls the behavior of humans around cats
"""

from ..api.cat import Cat

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
