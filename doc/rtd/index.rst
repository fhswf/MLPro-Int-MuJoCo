.. MLPro Documentations documentation master file, created by
   sphinx-quickstart on Wed Sep 15 12:06:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MLPro-Int-MuJoCo - Integration of MuJoCo into MLPro 
=================================================================

Welcome to MLPro-Int-MuJoCo, an extension to MLPro to integrate the MuJoCo package.
MLPro is a middleware framework for standardized machine learning in Python.
It is developed by the South Westphalia University of Applied Sciences, Germany, and provides standards, templates, and processes for hybrid machine learning applications.
MuJoCo (Multi-Joint dynamics with Contact), in turn, is a physics engine primarily used for simulating and optimizing complex robotic systems and physical interactions in various fields such as robotics, biomechanics, and machine learning.

MLPro-Int-MuJoCo offers wrapper classes that allow the reuse of functionalities from MuJoCo in MLPro.


**Preparation**

Before running the examples, please install the latest versions of MLPro and MuJoCo as follows:

.. code-block:: bash

   pip install mlpro-int-mujoco[full] --upgrade


**See also**
   - `MLPro - The integrative middleware framework for standardized machine learning in Python <https://mlpro.readthedocs.io>`_ 
   - `MLPro-BF - State-based Systems <https://mlpro.readthedocs.io/en/latest/content/02_basic_functions/mlpro_bf/sub/layer3_application_support/03_systems.html>`_
   - `MuJoCo - Advanced physics simulation <https://mujoco.org/>`_ 
   - `MLPro-Int-MuJoCo on GitHub <https://github.com/fhswf/MLPro-Int-MuJoCo>`_
   - `MLPro-Int-MuJoCo on PyPI <https://pypi.org/project/mlpro-int-mujoco>`_
   - `Further MLPro extensions <https://mlpro.readthedocs.io/en/latest/content/04_extensions/main.html>`_


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Home

   self


.. toctree::
   :maxdepth: 2
   :caption: Example Pool
   :glob:

   content/01_example_pool/*


.. toctree::
   :maxdepth: 2
   :caption: API Reference
   :glob:

   content/02_api/*


.. toctree::
   :maxdepth: 2
   :caption: About
   :glob:

   content/03_about/*

