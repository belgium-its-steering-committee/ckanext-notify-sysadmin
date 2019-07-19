.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/belgium-its-steering-committee/ckanext-notify-sysadmin.svg?branch=master
    :target: https://travis-ci.org/belgium-its-steering-committee/ckanext-notify-sysadmin

.. image:: https://coveralls.io/repos/belgium-its-steering-committee/ckanext-notify-sysadmin/badge.svg
  :target: https://coveralls.io/r/belgium-its-steering-committee/ckanext-notify-sysadmin

.. image:: https://pypip.in/download/ckanext-notify-sysadmin/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-notify-sysadmin/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-notify-sysadmin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-notify-sysadmin/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-notify-sysadmin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-notify-sysadmin/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-notify-sysadmin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-notify-sysadmin/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-notify-sysadmin/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-notify-sysadmin/
    :alt: License

=============
ckanext-notify-sysadmin
=============

notify sysadmins when new organisations are created


------------
Requirements
------------

Tested on CKAN 2.8.3


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-notify-sysadmin:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-notify-sysadmin Python package into your virtual environment::

     pip install -e  git+https://github.com/belgium-its-steering-committee/ckanext-notify-sysadmin#egg=ckanext-notify-sysadmin

3. Add ``notifysysadmin`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload



