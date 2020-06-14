SMTP = {"default": {}}
"""
SMTP server settings

Example settings::

    SMTP = {
        "default": {
            "host": "localhost",
            "port": 23,
            "username": None,
            "password": None,
        },
    }
"""


EMAIL = {"default": {}}
"""
Email Sender wrapper settings

Example settings::
    
     EMAIL = {
        "default": {
            "sender": "me@foo.com",
        }
     }

"""