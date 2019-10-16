# Django App Configuration Files

## [Django settings file](https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/app/app/settings.py)

A Django settings file contains all the configuration of your Django installation. This document explains how settings work and which settings are available. This is where we register any applications we create, the location of our static files, database configuration details, etc.

Sources: 

[Django Documentation](https://docs.djangoproject.com/en/2.2/topics/settings/)

[Django Tutorial Part 2: Creating a skeleton website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)

## [URL dispatcher](https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/app/app/urls.py)

A clean, elegant URL scheme is an important detail in a high-quality Web application. Django lets you design URLs however you want, with no framework limitations. While this could contain all the url mapping code, it is more common to delegate some of the mapping to particular applications.

Source: 

[Django Documentation](https://docs.djangoproject.com/en/2.2/topics/http/urls/)

[Django Tutorial Part 2: Creating a skeleton website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)

## [WSGI](https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/app/app/wsgi.py)

Django’s primary deployment platform is WSGI, the Python standard for web servers and applications. It helps your Django application communicate with the web server. 

Django’s startproject management command sets up a simple default WSGI configuration for you, which you can tweak as needed for your project, and direct any WSGI-compliant application server to use.

Django includes getting-started documentation for the following WSGI servers:

- How to use Django with Gunicorn
- How to use Django with uWSGI
- How to use Django with Apache and mod_wsgi
- Authenticating against Django’s user database from Apache

Source: [Django Documentation](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/)
