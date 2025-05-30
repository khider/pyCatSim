#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The cat module allows to create a Cat or a group of Cats (i.e. a Clowder)
"""

from .cat import Cat
                        
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
        nutmeg = cats.Cat('Nutmeg')
        charming = cats.Cat('Charming')
        maze = cats.Cat('Mazikeen')
        una = cats.Cat('Una')
        group = cats.Clowder(catlist = [nutmeg, charming, maze, una])
        
    """
        
    def __init__(self, catlist=None):
        if catlist is None:
             catlist = []
        elif isinstance(catlist, Cat):
            catlist = [catlist]
        elif not all(isinstance(cat,Cat) for cat in catlist):
            raise TypeError("All elements of the list must be a Cat object")
        self.catlist = catlist
        
        
    def add_cat(self, cat):
     
        """
        Adds a Cat to the Clowder

        Parameters
        ----------
        cat: pycCatSim.Cat
            the new Cat to add

        Raises
        ------
        TypeError
            If any of the arguments are not Cat instances.
        
        Examples
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat('Nutmeg')
            charming = cats.Cat('Charming')
            maze = cats.Cat('Mazikeen')
            una = cats.Cat('Una')
            group = cats.Clowder(catlist = [nutmeg, charming, maze, una])
            bailey = cats.Cat('Bailey')
            group.add_cat(bailey)
        
        """
    
        if not isinstance(cat, Cat):
                raise TypeError("Only Cat objects can be added.")
        self.catlist.append(cat)
    
    
    def remove_cat(self,cat):
        """
        Removes a Cat from the Clowder

        Parameters
        ----------
        cat: pyCatSim.Cat
            the Cat to remove

        Raises
        ------
        ValueError
            If the Cat is not found in the clowder.
        
        Examples
        --------
        
        .. jupyter-execute::
            
            import pyCatSim as cats
            nutmeg = cats.Cat('Nutmeg')
            charming = cats.Cat('Charming')
            maze = cats.Cat('Mazikeen')
            una = cats.Cat('Una')
            group = cats.Clowder(catlist = [nutmeg, charming, maze, una])
            group.remove_cat(nutmeg)
        """
        
        try:
            self.catlist.remove(cat)
        except ValueError:
            raise ValueError("Cat not found in Clowder")
