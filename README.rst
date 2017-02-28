=============================
instagram-app-client
=============================

.. image:: https://badge.fury.io/py/instagram-app-client.svg
    :target: https://badge.fury.io/py/instagram-app-client

.. image:: https://travis-ci.org/dmytrolitvinov/instagram-app-client.svg?branch=master
    :target: https://travis-ci.org/dmytrolitvinov/instagram-app-client

.. image:: https://codecov.io/gh/dmytrolitvinov/instagram-app-client/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dmytrolitvinov/instagram-app-client

A sample Django package

Documentation
-------------

The full documentation is at https://instagram-app-client.readthedocs.io.

Quickstart
----------

Install instagram-app-client::

    pip install instagram-app-client

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'instagram_app_client.apps.InstagramAppClientConfig',
        ...
    )

Add instagram-app-client's URL patterns:

.. code-block:: python

    from instagram_app_client import urls as instagram_app_client_urls


    urlpatterns = [
        ...
        url(r'^', include(instagram_app_client_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
