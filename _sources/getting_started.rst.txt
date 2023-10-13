Getting Started
===============

This page details how to get started with waterdynamics. 

Installation
------------

PyPi
~~~~

The waterdyanmics package can be installed from PyPI with:

.. code-block:: bash

	pip install waterdynamics

If you would like to test your installation, use the `test` optional dependencies and run the tests:

.. code-block:: bash

	pip install "waterdynamics[test]"
	pytest --pyargs waterdynamics.tests

From source
~~~~~~~~~~~

If you want the latest (non-release) version of waterdynamics, you should install the package from source.

.. code-block:: bash

	git clone https://github.com/MDAnalysis/waterdynamics
	cd waterdynamics
	pip install .

If you want to run tests on your installation, install the `test` dependencies and run the tests:

.. code-block:: bash

	pip install ".[test]"
	pytest --pyargs waterdynamics.tests

