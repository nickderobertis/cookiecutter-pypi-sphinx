.. {{ cookiecutter.repo_name }} documentation master file, created by
   cookiecutter-pypi-sphinx.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.full_name }} documentation!
********************************************************************

{{ cookiecutter.short_description }}

To get started, look here.

.. toctree::
   :caption: Tutorial

   tutorial
   auto_examples/index

An overview
===========

Quick Links
------------

Find the source code `on Github <https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}>`_.


{{ cookiecutter.package_name }}
-------------------------------------------------------


This is a simple example:

.. code:: python

    import {{ cookiecutter.package_directory }}


.. toctree:: api/modules
   :caption: API Documentation
   :maxdepth: 3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
