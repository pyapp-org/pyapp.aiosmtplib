"""
SMTP Client Factory
~~~~~~~~~~~~~~~~~~~

"""
from aiosmtplib import SMTP
from pyapp.conf.helpers import NamedFactory

__all__ = ("factory", "get_client", "SMTP")


class SMTPFactory(NamedFactory[SMTP]):
    """
    Factory for SMTP connections
    """

    defaults = {
        "hostname": "localhost",
        "use_tls": False,
        "start_tls": False,
        "validate_certs": True,
        "timeout": 60,
    }
    optional_keys = (
        "port",
        "username",
        "password",
        "source_address",
        "client_cert",
        "client_key",
        "cert_bundle",
    )

    def create(self, name: str = None) -> SMTP:
        """
        Create an SMTP client instance
        """
        config = self.get(name)
        return SMTP(**config)

    # Doesn't currently support async
    # def check_definition(
    #     self, config_definitions: Dict[str, Any], name: str, **_
    # ) -> Union[CheckMessage, Iterable[CheckMessage]]:
    #     messages = super().check_definition(config_definitions, name)
    #
    #     # If there are any serious messages don't bother with connectivity check
    #     if any(m.is_serious() for m in messages):
    #         return messages
    #
    #     try:
    #         with self.create(name) as client:
    #             client.smtp.noop()
    #     except Exception as ex:
    #         messages.append(
    #             Error(
    #                 "SMTP connection check failed",
    #                 f"Check connection parameters, exception raised: {ex}",
    #                 f"settings.{self.setting}[{name}]",
    #             )
    #         )
    #
    #     return messages


factory = SMTPFactory("SMTP")
get_client = factory.create
