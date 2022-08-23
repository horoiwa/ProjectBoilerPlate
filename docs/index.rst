.. project documentation master file, created by
   sphinx-quickstart on Sun Aug  7 14:00:57 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to project's documentation!
===================================

.. toctree::
   :maxdepth: 4

   modules


Mermaid integration
===================

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!

|


Jupyter integration
=====================

.. toctree::
    :maxdepth: 4

    notebooks/sample.ipynb

|


Use markdown
==============

.. toctree::
    :maxdepth: 4

   Note.md

|

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


About
=======

.. toctree::
   :maxdepth: 2

   about.rst

   Note.md
