from nose.plugins import Plugin
from blessings import Terminal


class NoseRapidoNotifier(Plugin):
    """
    Rapid feedback notifier for Nose

    Colors your terminal (green|blue) or red depending on test result.
    For better experience, use with a watch tool such as nose-watch
    """

    name = 'rapido'

    def options(self, parser, env=None):
        Plugin.options(self, parser, env)
        parser.add_option('--rapido-blue', action='store_true',
                          dest='rapido_blue',
                          default=False,
                          help=
                          "Use the color blue instead of \
green for successfull tests")

    def configure(self, options, config):
        Plugin.configure(self, options, config)
        self.rapido_blue = options.rapido_blue

    def finalize(self, result):
        term = Terminal()
        #TODO: Calulate if enough screen estate to print out:
        #testsRun, errors, failures, skipped

        color_fcn = None
        if result.wasSuccessful():
            color_fcn = term.green_on_green if not self.rapido_blue \
                else term.blue_on_blue
        else:
            color_fcn = term.red_on_red
        the_string = color_fcn(
            (" " * term.width).join(["\n"] * (term.height + 1))[:-1])
        with term.location(0, 0):
            self.print_to_screen(
                "{clear}{chars}".format(
                    clear=term.clear,
                    chars=the_string))

    def print_to_screen(self, what):
        # Separated for testability
        print what,
