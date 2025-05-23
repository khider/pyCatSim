.. _installing_pycatsim:

.. note::

   PyCatSim requires the use of Python 3.12 or above

Installing PyCatSim 
====================

If you know what you are doing, you may install PyCatSim in any suitable Python environment, with a Python version >=3.12.

However, we have not and cannot possibly, try every situation. 

If you are new to Python, we recommend the use of Anaconda (or its minimal version Miniconda), to set up such an environment. Then you may install PyCatSim via pip.


Installing Anaconda or Miniconda
"""""""""""""""""""""""""""""""""

To install Anaconda or Miniconda on your platform, follow the instructions from `this page <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`_.

Creating a new conda environment
"""""""""""""""""""""""""""""""""""
As of June 2025, we recommend Python 3.12. Create an environment via the command line (e.g. Terminal app in MacOS):

.. code-block:: bash

  conda create -n cat python=3.12

To view a list of available environments:

.. code-block:: bash

  conda env list

To activate the new environment:

.. code-block:: bash

  conda activate cat

To view the list of packages in your environment:

.. code-block:: bash

  conda list

To remove the environment:

.. code-block:: bash

  conda remove --name cat --all

More information about managing conda environments can be found `here <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#>`_.

Installing PyCatSim
""""""""""""""""""""
Once the pyleo environment is activated, simply run:

.. code-block:: bash

  pip install pyCatSim

This will install the latest official release, which you can view `here <https://pypi.org/project/pyCatSim/>`_. To install the latest version, which contains the most up-to-date features, you can install directly from the GitHub source:

.. code-block:: bash

  pip install git+https://github.com/khider/pyCatSim.git

This version may contain bugs not caught by our continuous integration test suite; if so, please report them via `github issues <https://github.com/khider/pyCatSim/issues>`_

If you would like to use Spyder for code development:

.. code-block:: bash

  conda install spyder
  
If you intend on using PyCatSim within a Jupyter Notebook, we recommend using `ipykernel <https://anaconda.org/anaconda/ipykernel>`_.   
  
.. code-block:: bash

  conda install ipykernel    
  python -m ipykernel install --user --name=cat       
  
The first line will install ipykernel and its dependencies, including IPython, Jupyter, etc. The second line will make sure the pyleo environment is visible to Jupyter (see `this page for context <https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove>`_)
