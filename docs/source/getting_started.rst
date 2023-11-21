Getting Started
===============

Install the ``waterdynamics`` package by any of the methods described below:

Installation
------------

From conda-forge
~~~~~~~~~~~~~~~~

Install `waterdynamics from the conda-forge channel <https://anaconda.org/conda-forge/waterdynamics>`_
by first adding ``conda-forge`` to you channels with:

.. code-block:: sh

	conda config --add channels conda-forge
	conda config --set channel_priority strict

Once the ``conda-forge`` channel has been enabled, ``waterdynamics`` can be installed with :program:`conda`:

.. code-block:: sh

	conda install waterdynamics

or with :program:`mamba` (if you have it installed):

.. code-block:: sh

	mamba install waterdynamics

From the Python Package Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The waterdynamics package can be installed from PyPI with:

.. code-block:: sh

	pip install waterdynamics

If you would like to test your installation, use the `test` optional dependencies and run the tests:

.. code-block:: sh

	pip install "waterdynamics[test]"
	pytest --pyargs waterdynamics.tests

From source
~~~~~~~~~~~

If you want the latest (non-release) version of waterdynamics, you should install the package from source.

.. code-block:: sh

	git clone https://github.com/MDAnalysis/waterdynamics
	cd waterdynamics
	pip install .

If you want to run tests on your installation, install the `test` dependencies and run the tests:

.. code-block:: sh

	pip install ".[test]"
	pytest --pyargs waterdynamics.tests

