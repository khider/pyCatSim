
# __all__=['random_facts']

import random

def random_facts():
    """
    calls up random facts about cats

    Returns
    -------
    str
        A fact randomly chosen from a pre-defined fact pool 

    """

    cat_facts = [
        "Cats sleep for 70% of their lives.",
        "A group of cats is called a clowder.",
        "Cats can rotate their ears 180 degrees.",
        "The world's oldest cat lived to be 38 years old.",
        "Cats have five toes on their front paws, but only four on the back.",
        "A cat can jump up to six times its length.",
        "Each cat's nose print is unique, like a human fingerprint.",
        "Cats use their whiskers to detect changes in their surroundings.",
        "The average house cat can run at speeds up to 30 mph.",
        "Cats meow only to communicate with humans."
    ]
    return random.choice(cat_facts)


