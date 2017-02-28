=====
Usage
=====

To use instagram-app-client in a project, add it to your `INSTALLED_APPS`:

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
