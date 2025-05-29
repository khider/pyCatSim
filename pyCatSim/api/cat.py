#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The cat module allows to create a Cat or a group of Cats (i.e. a Clowder)
"""


from ..utils import noises

import difflib

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
            The sound the cat makes. Valid options include "meow", "purr". The default is 'meow'.
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
        
        Examples
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
            nutmeg.make_noise()

        """
        
        noise_func ={
            'meow':noises.meow,
            'purr':noises.purr}
    
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


                        
        
        