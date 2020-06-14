from email.message import EmailMessage, Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Sequence, Union, Optional

from aiosmtplib import SMTPResponse
from pyapp.conf.helpers import ThreadLocalNamedSingletonFactory

from .factory import get_client


class Email:
    """
    SMTP Client wrapper that handles
    """

    def __init__(self, *, sender: str = None, name: Optional[str] = None):
        self.sender = sender
        self.name = name

        self._client = get_client(self.name)

    async def send_message(
        self,
        message: Message,
        recipients: Union[str, Sequence[str]],
        sender: str = None,
    ) -> SMTPResponse:
        """
        Send message
        """
        async with self._client:
            return self._client.send_message(
                message, sender or self.sender, recipients
            )

    async def send_plain(
        self,
        recipients: Union[str, Sequence[str]],
        subject: str,
        body: str,
        sender: str = None,
    ):
        """
        Send a plain message
        """
        message = EmailMessage()
        message["Subject"] = subject
        message.set_content(body)

        return await self.send_message(
            message, recipients, sender or self.sender
        )

    async def send(
        self,
        recipients: Union[str, Sequence[str]],
        subject: str,
        body: str,
        html_body: str = None,
        sender: str = None,
    ):
        """
        Send a multipart message with both text and HTML
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        if html_body:
            message.attach(MIMEText(html_body, "html"))

        return await self.send_message(
            message, recipients, sender or self.sender
        )


class EmailFactory(ThreadLocalNamedSingletonFactory[Email]):
    """
    Factory for Email instances
    """

    optional_keys = (
        "sender",
    )

    def create(self, name: str = None) -> Email:
        """
        Create an SMTP client instance
        """
        config = self.get(name)
        return Email(**config)


email_factory = EmailFactory("EMAIL")
get_sender = email_factory.create
