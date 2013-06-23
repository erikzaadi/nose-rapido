from unittest import TestCase
from noserapido import NoseRapidoNotifier
from mock import MagicMock, patch


class TestNoseRapidoLed(TestCase):

    def _get_instance(self, config=None):
        if config is None:
            config = MagicMock()
            config.rapido_blue = False
        instance = NoseRapidoNotifier()
        instance.configure(config, MagicMock())
        instance.print_to_screen = MagicMock()

        return instance

    def _prepare_terminal_mock(self, mock_terminal):
        mock_terminal_instance = MagicMock()
        mock_terminal.return_value = mock_terminal_instance

        mock_terminal_instance.clear = "[CLEAR]"
        mock_terminal_instance.height = 3
        mock_terminal_instance.width = 5

        return mock_terminal_instance

    @patch("noserapido.Terminal")
    def test_notify_called_with_red_on_fail(self, mock_terminal):
        instance = self._get_instance()

        mock_terminal_instance = self._prepare_terminal_mock(mock_terminal)

        mock_terminal_instance.red_on_red.return_value = "[ON_RED]"

        result = MagicMock()
        result.wasSuccessful.return_value = False

        instance.finalize(result)
        instance.print_to_screen.assert_called_once_with(
            mock_terminal_instance.clear +
            mock_terminal_instance.red_on_red.return_value)

    @patch("noserapido.Terminal")
    def test_notify_called_with_green_on_success(self, mock_terminal):
        instance = self._get_instance()

        mock_terminal_instance = self._prepare_terminal_mock(mock_terminal)
        mock_terminal_instance.green_on_green.return_value = "[ON_GREEN]"

        result = MagicMock()
        result.wasSuccessful.return_value = True

        instance.finalize(result)
        instance.print_to_screen.assert_called_once_with(
            mock_terminal_instance.clear +
            mock_terminal_instance.green_on_green.return_value)

    @patch("noserapido.Terminal")
    def test_notify_called_with_blue_if_flag_on_success(self, mock_terminal):
        config = MagicMock()
        config.rapido_blue = True
        instance = self._get_instance(config)

        mock_terminal_instance = self._prepare_terminal_mock(mock_terminal)
        mock_terminal_instance.blue_on_blue.return_value = "[ON_BLUE]"

        result = MagicMock()
        result.wasSuccessful.return_value = True

        instance.finalize(result)
        instance.print_to_screen.assert_called_once_with(
            mock_terminal_instance.clear +
            mock_terminal_instance.blue_on_blue.return_value)
