import os
import random
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

__all__=['show']

# Path to the sound files
IMG_DIR = Path(__file__).parents[1].joinpath("images").resolve()


def show(color):
    """
    

    Parameters
    ----------
    color : TYPE
        DESCRIPTION. 

    Returns
    -------
    None.

    """
    


    filename = f"{color}.jpg"
    image_path = os.path.join(IMG_DIR, filename)
    

    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
