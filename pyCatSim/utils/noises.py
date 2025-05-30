#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains possible sounds cats can make
"""


__all__=['meow',
         'purr',
         'chatter',
         'chirrup',
         'hiss']

from playsound import playsound
import os
from pathlib import Path 


# Path to the sound files
SOUND_DIR = Path(__file__).parents[1].joinpath("sounds").resolve()

def meow(play=False):
    """
    Simulates a meow

    Parameters
    ----------
    play : Bool, optional
        Whether to play the sound (True) or display the text (False). The default is False.

    Returns
    -------
    str
        If play is False, returns the sound as text

    """
    
    if play is False:
        return "Meow!"
    else:
        playsound(os.path.join(SOUND_DIR, "meow.mp3"))

def purr(play=False):
    """
    Simulates a purr

    Parameters
    ----------
    play : Bool, optional
        Whether to play the sound (True) or display the text (False). The default is False.

    Returns
    -------
    str
        If play is False, returns the sound as text

    """
    
    if play is False:
        return "Purrr"
    else:
        playsound(os.path.join(SOUND_DIR, "purr.mp3"))

def chatter(play=False):
    """
    Simulates a chatter
    
    Parameters
    ----------
    play : Bool, optional
        Whether to play the sound (True) or display the text (False). The default is False.

    Returns
    -------
    str
        If play is False, returns the sound as text
    """
    
    if play is False:
        return "chattering"
    else:
        playsound(os.path.join(SOUND_DIR, "chattering.mp3"))

def chirrup(play=False):
    """
    Simulates a chirrup

    Parameters
    ----------
    play : Bool, optional
        Whether to play the sound (True) or display the text (False). The default is False.

    Returns
    -------
    str
        If play is False, returns the sound as text

    """
        
    if play is False:
        return "Chirrup"
    else:
        playsound(os.path.join(SOUND_DIR, "chirrup.mp3"))

def hiss(play=False):
    """
    Simulates a hiss
    
    Parameters
    ----------
    play : Bool, optional
        Whether to play the sound (True) or display the text (False). The default is False.

    Returns
    -------
    str
        If play is False, returns the sound as text
    
    """
    if play is False:
        return "Hiss.."
    else:
        playsound(os.path.join(SOUND_DIR, "hissing.mp3"))
