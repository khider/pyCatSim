#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The human module controls the behavior of humans around cats
"""

try:
    from ..api.cat import Cat
except ImportError:
    class Cat:
        """
        Represents a cat with name, hunger, and mood attributes.

        Parameters
        ----------
        name : str
            The name of the cat.

        Attributes
        ----------
        name : str
            The name of the cat.
        hunger : int
            The current hunger level of the cat (lower is better).
        mood : int
            The current mood level of the cat (higher is better).
        """
        def __init__(self, name):
            self.name = name
            self.hunger = 0
            self.mood = 0

        def play(self):
            """
            Play with the cat, increasing its mood by 2 and hunger by 1.
            """
            self.mood += 2
            self.hunger += 1

        def pet(self):
            """
            Pet the cat, increasing its mood by 1.
            """
            self.mood += 1

        def status(self):
            """
            Return a string representing the cat's current status.

            Returns
            -------
            str
                A string describing the cat's name, hunger, and mood.
            """
            return f"{self.name}: Hunger={self.hunger}, Mood={self.mood}"

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
            If the cat does not have 'hunger' or 'mood' attributes.
        """
        if cat not in self.cats_owned:
            raise ValueError("This owner does not own the specified cat.")
        if not hasattr(cat, 'hunger') or not hasattr(cat, 'mood'):
            raise AttributeError("Cat must have 'hunger' and 'mood' attributes.")

        cat.hunger = max(0, cat.hunger - 1)
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

# Example test function
def test_feed():
    """
    Unit test for the Owner.feed() method.
    """
    kitty = Cat(name="TestCat")
    kitty.hunger = 2
    kitty.mood = 5

    owner = Owner(name="TestOwner", cats_owned=kitty)
    print(f"Before feeding: Hunger={kitty.hunger}, Mood={kitty.mood}")
    owner.feed(kitty)
    print(f"After feeding: Hunger={kitty.hunger}, Mood={kitty.mood}")

    assert kitty.hunger == 1, "Hunger should decrease by 1"
    assert kitty.mood == 6, "Mood should increase by 1"
    print("test_feed passed!")

if __name__ == "__main__":
    test_feed()