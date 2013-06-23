===========
nose-rapido
===========

.. image:: https://secure.travis-ci.org/erikzaadi/nose-rapido.png?branch=master
    :target: http://travis-ci.org/erikzaadi/nose-rapido

A Nose plugin that allows to get rapid feedback from tests, by filling your terminal either with green (can be changed to blue) or red background, depending on your tests result.

Use together with a continuous running test plugin such as `nose-watch <https://github.com/lukaszb/nose-watch>`_ for optimal results.


Installation
============
::

    pip install nose-rapido


How to use
==========

In order to use this plugin use the ``--with-rapido`` switch::

    nosetests --with-rapido

**NOTE:** nose-rapido will override any output you have from other plugins.

You can also replace the color green for successfull tests to blue (easier to see for colorblinded)::

    nosetests --with-rapido --rapido-blue

Screenshots
===========

Good

.. image:: https://github.com/erikzaadi/nose-rapido/raw/master/screenshots/good.png
    :target: https://github.com/erikzaadi/nose-rapido/blob/master/screenshots/good.png

Bad

.. image:: https://github.com/erikzaadi/nose-rapido/raw/master/screenshots/bad.png
    :target: https://github.com/erikzaadi/nose-rapido/blob/master/screenshots/bad.png

Blue

.. image:: https://github.com/erikzaadi/nose-rapido/raw/master/screenshots/blue.png
    :target: https://github.com/erikzaadi/nose-rapido/blob/master/screenshots/blue.png

Development
===========

Preferably in a virtualenv::

    pip install -r requirements-dev.txt
    nosetests --with-watch
    #or
    tox
