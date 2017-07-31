=============================
Readme
=============================

Client-side app for instagram stream.

Configuration
-------------

Django
======

- :code:`INSTAGRAM_APP_ID` --- App ID. Default 1.
- :code:`INSTAGRAM_STREAM_CACHING_BACKEND` --- Caching backend for :code:`requests-cache`. Default :code:`'memory'`.
    `Docs <https://requests-cache.readthedocs.io/en/latest/user_guide.html#persistence>`_.

Constance
=========


.. code-block:: python

    CONSTANCE_CONFIG = {
        'INSTAGRAM_STREAM_URL': (
            'http://stream.dillysocks.com/',
            u'Instagram steam URL (applied to all widgets)',
        ),
        'INSTAGRAM_STREAM_ENABLED': (
            True,
            u'Enable or disable all instagram widgets',
        ),
        'INSTAGRAM_STREAM_ENABLE_CACHING': (
            True,
            u'Enable or disable caching',
        ),
        'INSTAGRAM_STREAM_CACHE_EXPIRATION': (
            600,
            u'Instagram cache expiration (in seconds). 10 minutes by default',
        ),
    }
