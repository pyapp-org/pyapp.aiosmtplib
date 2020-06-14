##################
pyApp - aioSMTPlib
##################

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: http://github.com/ambv/black
   :alt: Once you go Black...

.. image:: https://api.codeclimate.com/v1/badges/e25e476cd1cd598e89f4/maintainability
   :target: https://codeclimate.com/github/pyapp-org/pyapp.aiosmtplib/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/e25e476cd1cd598e89f4/test_coverage
   :target: https://codeclimate.com/github/pyapp-org/pyapp.aiosmtplib/test_coverage
   :alt: Test Coverage

This extension provides an Async `SMTP` client object configured via pyApp settings.


Installation
============

Install with *pip*::

    pip install pyApp-aiosmtplib


Add the `SMTP` block into your runtime settings file::

    SMTPLIB = {
        "default": {
            "host": "localhost",
        }
    }


.. note::

    In addition to the *host* any argument that can be provided to
    `aiosmtplib.SMTP` can be provided.


Usage
=====

The following example creates an SMTP client instance::

    from pyapp_ext.aiosmtplib import get_client

    smtp = get_client()


API
===

`pyapp_ext.aiosmtplib.get_client() -> SMTP`

    Get named `SMTP` instance.

