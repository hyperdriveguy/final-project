import arcade
from game.overworld import Overworld

class MainWindow(arcade.Window):
    """
    Main application class.

    Stereotype: Controller, Interfacer
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.overworld = Overworld()
        self.show_view(self.overworld)


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key in (arcade.key.F11, arcade.key.P):
            self.set_fullscreen(not self.fullscreen)

            self.overworld.camera.resize(self.width, self.height)
            self.overworld.gui_camera.resize(self.width, self.height)
                