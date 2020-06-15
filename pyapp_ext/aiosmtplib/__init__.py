"""
pyApp AIOSTMPlib Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from pyapp.app import CommandGroup, argument

from .factory import *


class Extension:
    """
    SMTP Extension
    """

    default_settings = ".default_settings"
    checks = ".checks"

    @staticmethod
    def register_commands(root: CommandGroup):
        group = root.create_command_group("email")
        group.command(Extension.send)

    @staticmethod
    @argument("-r", "--recipient", action="append", help_text="Message recipient(s)")
    @argument("-S", "--sender", dest="sender", help_text="Message sender")
    @argument("-s", "--subject", help_text="Message subject")
    @argument("-b", "--body", default="Test Email", help_text="Message body; defaults to 'Test Email'")
    @argument(
        "--config", default="default", help_text="Email configuration to use."
    )
    def send(opts):
        """
        Send a test email
        """
        from .helpers import get_sender
        get_sender().send_plain(
            opts.TO, opts.SUBJECT, opts.body or "Test Email", from_=opts.from_
        )
