#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The cat module allows to create a Cat or a group of Cats (i.e. a Clowder)
"""


from ..utils import noises
from ..utils import facts

import difflib
import math

class Cat:
    
    """
    Represents a virtual cat with attributes like name, age, color, mood, hunger, energy, and health.
    
    Parameters
    ----------
    name : str
        The name of the cat.
    age : int, optional
        The age of the cat in years. Default is None.
    color : str, optional
        Coat color of the cat. Acceptable values are:
        'tabby', 'black', 'orange', 'tortoiseshell', and 'tuxedo'.
        Fuzzy matching is used to interpret close inputs. Default is None.
    mood : int, optional
        Mood level on a scale from -10 (grumpy) to 10 (ecstatic). Default is 0.
    hunger_level : int, optional
        Hunger level of the cat. Higher values indicate greater hunger. Default is 0.
    energy : int, optional
        Energy level of the cat. Default is 0.
    health : int, optional
        Health level of the cat. Default is 0.

    Attributes
    ----------
    name : str
        The name of the cat.
    age : int or None
        The age of the cat.
    color : str or None
        The interpreted or validated color of the cat.
    mood : int
        The cat's mood.
    hunger_level : int
        The cat's hunger level.
    energy : int
        The cat's energy level.
    health : int
        The cat's health level.
    
    
    Examples
    --------
    
    .. jupyter-execute::
        
        import pyCatSim as cats
        nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
    
    """

    def give_fact(self):
        """
        calls ..utils.random_facts() and return a random fact about cats
        
        Returns
        -------
        str
            A fact randomly chosen from a pre-defined fact pool 
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            nutmeg.give_fact()
        """ 
        return facts.random_facts()
    
    def __init__(self, name, age=None, color=None, mood=0, hunger_level=0, 
                 energy=0, health=0):
        
        
        self.name = name
        self.age = age
        
        possible_colors = ['tabby', 'black', 'orange', 'tortoiseshell', 'tuxedo']

        if color:
            color_normalized = color.lower().strip()
            match = difflib.get_close_matches(color_normalized, possible_colors, n=1, cutoff=0.6)

            if match:
                self.color = match[0]
                print(f"Color '{color}' interpreted as '{self.color}'.")
            else:
                print(f"Invalid color '{color}'. Valid options are: {', '.join(possible_colors)}.")
                self.color = None
        
        self.mood = mood
        self.hunger_level = hunger_level
        self.energy = energy
        self.health = health
    
    def make_noise(self, noise='meow', play=False):
        """
        

        Parameters
        ----------
        noise : string, optional
            The sound the cat makes. Valid options include "meow", "purr", "chirrup", and "hiss". The default is 'meow'.

        play : bool, optional
            Whether to play the sound (True) or print out the sound (False). The default is False.

        Raises
        ------
        ValueError
            Raises an error if the sound is not valid

        Returns
        -------
        str
            The sound
        
        See also
        --------
        
        pyCatSim.utils.noises.meow: Simulates a cat meow
        
        pyCatSim.utils.noises.purr: Simulates a cat purr

        pyCatSim.utils.noises.hiss: Simulates a cat hiss
        
        pyCatSim.utils.noises.chirrup: Simulates a cat chirrup

        
        Examples
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            nutmeg.make_noise()

        """
        
        noise_func ={
            'meow':noises.meow,
            'purr':noises.purr,
            'hiss':noises.hiss,
            'chirrup':noises.chirrup}
    
        if noise in noise_func.keys():
            return noise_func[noise](play=play)
        else:
            raise ValueError(f"Invalid noise '{noise}'. Valid options: {', '.join(noise_func.keys())}")
        
        
    def play(self, mood_boost=1, hunger_boost=1, energy_boost=-1):
            
            """
            Simulates playtime with the cat.
        
            Parameters
            ----------
            mood_boost : int, optional
                How much mood improves from play. Must be an integer. Default is 1.
            hunger_boost : int, optional
                How much hunger increases from play. Must be a positive integer. Default is 1.
            energy_boost : int, optional
                How much energy decreases from play. Must be a negative integer. Default is -1.
        
            Raises
            ------
            TypeError
                If any of the arguments are not integers.
            ValueError
                If hunger_boost is not positive or energy_boost is not negative.
                
            Examples
            --------
            
            .. jupyter-execute::
                
                import pyCatSim as cats
                nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
                nutmeg.play()
                
            
            """
            for arg_name, arg_value in {
                "mood_boost": mood_boost,
                "hunger_boost": hunger_boost,
                "energy_boost": energy_boost
            }.items():
                if not isinstance(arg_value, int):
                    raise TypeError(f"{arg_name} must be an integer.")
        
            if hunger_boost <= 0:
                raise ValueError("Cats always get hungry when playing! hunger_boost must be positive.")
            if energy_boost >= 0:
                raise ValueError("Cats always get tired when playing! energy_boost must be negative.")
        
            self.mood += mood_boost
            self.hunger_level += hunger_boost
            self.energy += energy_boost
            
    def bathe(self):
        """
        Bathes the cat, decreasing mood and improving health.

        Cats typically dislike baths, which lowers their mood,
        but it improves their cleanliness and boosts health.

        Effects
        -------
        - mood: decreases by 1
        - health: increases by 1

        Examples
        --------
        .. jupyter-execute::

            import pyCatSim as cats
            mochi = cats.Cat(name='Mochi', mood=3, health=5)
            mochi.bathe()
            print(mochi.mood)   # Output: 2
            print(mochi.health) # Output: 6
        """
        self.mood -= 1
        self.health += 1

                        
    def groom(self):
            
            """
            Grooms a cat, increasing its health and mood levels by one unit.
        
            
            Examples
            --------
            
            .. jupyter-execute::
                
                import pyCatSim as cats
                nutmeg = cats.Cat(name = 'Nutmeg', age = 3, color = 'tortoiseshell')
                nutmeg.groom()
                
            
            """
            self.mood += 1
            self.health += 1
            print(f"{self.name} has been groomed. Health: {self.health}, Mood: {self.mood}")
    
    def eat(self):
        """
        Feeds the cat by reducing its hunger level and improving its mood.

        When called:
        - Decreases `hunger_level` by 1 (to a minimum of 0).
        - Increases `mood` by 1.

        Returns
        -------
        dict
            A dictionary containing the updated `hunger_level` and `mood`.

        Examples
        --------
        .. jupyter-execute::

            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', hunger_level=2, mood=0)
            nutmeg.eat()
            # Output: {'hunger_level': 1, 'mood': 1}
        """
        # Prevent hunger_level from going negative
        if self.hunger_level > 0:
            self.hunger_level -= 1
        else:
            self.hunger_level = 0

        self.mood += 1
        # Optionally, return the new state
        return {"hunger_level": self.hunger_level, "mood": self.mood}


    def sleep(self, duration=0):
        """
        Simulates the cat getting some sleep.

        Sleep() causes the cat to sleep for an optionally-specified duration (hrs; default=0).
        For every 3 hours the cat sleeps, its energy level increases increases by 1 (rounded down
        to the nearest integer). For example, having the cat sleeping for a duration of 5 hours raises
        its energy level by 1.

        Parameters
        ----------
        duration : int or float, optional
            Number of hours the cat sleeps. Must be an integer or float. The default is 0.

        Raises
        ------
        TypeError
            If duration is neither an integer nor float.
        ValueError
            If duration is not positive or is greater than 16.
        
        Examples
        --------
        
        ..jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            nutmeg.sleep(duration=5)

        """

        # Enforce duration type is int or float
        if type(duration) != int:
            if type(duration) != float:
                raise TypeError("duration must be an integer or float")

        # Enforce min (0 hrs) and max duration (16 hrs)
        if duration < 0:
            raise ValueError("Cats cannot sleep for negative hours. User-specified duration must be positive")
        if duration > 16:
            raise ValueError("Cats should not sleep for more than 16 hours. User-specified duration must be less than 16")

        # Cat gains 1 energy level for every 3 hours of sleep (rounded-down; floor())
        energy_boost = math.floor(duration/3)

        self.energy += energy_boost
                        
class Clowder:
    """
    Represents a group of cats.
    
    Parameters
    ----------
    catlist: list 
        A list of cats from the Cat class

    Attributes
    ----------
    catlist: list 
        A list of cats from the Cat class
    
    Examples
    --------
    
    .. jupyter-execute::
        
        import pyCatSim as cats
        group = cats.Clowder(catlist = [list_of_Cats])
    """
        
    def __init__(self, catlist=None):
        if catlist is None:
             catlist = []
        elif not all(isinstance(cat,Cat) for cat in catlist):
            raise TypeError("All elements of the list must be a Cat object")
        self.catlist = catlist
        
        
    def add_cat(self, cat):
     
        """
        Adds a Cat to the Clowder

        Parameters:
        -----------
        cat: Cat
            the new Cat to add

        Raises
        ------
        TypeError
            If any of the arguments are not Cat instances.
        """
    
        if not isinstance(cat, Cat):
                raise TypeError("Only Cat objects can be added.")
        self.catlist.append(cat)
    
    
    def remove_cat(self,cat):
        """
        Removes a Cat from the Clowder

        Parameters:
        -----------
        cat: Cat
            the Cat to remove

        Raises
        ------
        ValueError
            If the Cat is not found in the clowder.
        """
        
        try:
            self.catlist.remove(cat)
        except ValueError:
            raise ValueError("Cat not found in Clowder")
