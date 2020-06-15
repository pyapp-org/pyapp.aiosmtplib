from unittest.mock import Mock

from pyapp_ext.aiosmtplib import helpers


class TestEmail:
    def test_init(self, monkeypatch):
        mock_factory = Mock()
        monkeypatch.setattr(helpers, "get_client", mock_factory)

        helpers.Email(name="foo")

        mock_factory.assert_called_with("foo")
