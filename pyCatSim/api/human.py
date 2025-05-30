#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The human module controls the behavior of humans around cats
"""

from ..api.cat import Cat
from ..utils import facts


class Owner:
    """
    Represents a cat owner who can care for one or more cats

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
    
    def give_fact(self):
        """
        Gives a random fact about cats
        
        Returns
        -------
        str
            A fact randomly chosen from a pre-defined fact pool 
        
        Examples
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            nutmeg.give_fact()
        """ 
        return facts.random_facts()

    def feed(self, cat):
        """
        Feed the specified cat owned by this Owner. Decreases `hunger_level` by 1 and Increases `mood` by 1.

        Parameters
        ----------
        cat : pyCatSim.Cat
            The cat to feed. Must be owned by this owner.

        Raises
        ------
        ValueError
            If the specified cat is not owned by this owner.
        AttributeError
            If the cat does not have 'hunger_level' or 'mood' attributes.
            
        
        ..jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            john = cats.Owner(name='John', cats_owned = nutmeg)
            john.feed(nutmeg)
    
            
        """
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        if not hasattr(cat, 'hunger_level') or not hasattr(cat, 'mood'):
            raise AttributeError("Cat must have 'hunger_level' and 'mood' attributes.")

        cat.hunger_level = max(0, cat.hunger_level - 1)
        cat.mood += 1

    def adopt(self, cats):

        """
        Add a Cat object or a list of Cat objects to an owner's cats.

        Parameters
        ----------
        cats: pyCatSim.Cat or list
            the cat(s) to be added to the list

        Raises
        ------
        TypeError
                If any of the arguments are not Cat.
        ValueError
                If cats_object is not Cat.

        Examples
        --------

        .. jupyter-execute::

            import pyCatSim as cats

            cat1 = cats.Cat(name="Whiskers")
            cat2 = cats.Cat(name="Boots", color="tabby")
            owner1 = cats.Owner(name="Sasha", cats_owned=cat1)
            owner2 = cats.Owner(name="Liam", cats_owned=[cat1, cat2])

            chestnut = cats.Cat(name='Chestnut', age = 4, color = 'tabby')
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            owner1.adopt(nutmeg)
            owner2.adopt([chestnut,nutmeg])

            print([cat.name for cat in owner2.cats_owned])


        """
        if isinstance(cats, Cat):
            self.cats_owned.append(cats)
        elif isinstance(cats, list):
            if not all(isinstance(cat, Cat) for cat in cats):
                raise TypeError("All elements in cats_object must be instances of Cat.")
            else:
                self.cats_owned+=cats
        else:
            raise TypeError("cats_owned must be a Cat instance or a list of Cat instances.")

        
    def groom(self,Cat):
        """
        Simulates an owner grooming one cat, increasing its mood by one

        Parameters
        ----------
        Cat : pyCatSim.Cat
            a Cat object that you would like to groom.

        Returns
        -------
        None.

        
        Examples
        --------
        .. jupyter-execute::
        
            from pyCatSim import Cat, Owner
            cat1 = Cat(name="Whiskers")
            Deborah = Owner(name="Deborah", cats_owned=cat1)
            Deborah.groom(cat1)

        """
        
        Cat.mood += 1
 
