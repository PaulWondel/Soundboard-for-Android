"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from playsound import playsound


class Soundboardforandroid(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        
        # Doesn't work yet, gives an weird error
        # sound_button = toga.Button(
        #     'Sound Test',
        #     on_press=self.play_track,
        #     style=Pack(padding=5)
        # )

        main_box.add(name_box)
        main_box.add(button)
        # main_box.add(sound_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = 'stranger'

        self.main_window.info_dialog(
            'Response',
            "Hello, {}.\nYou're looking stunning today.".format(name)
        )
    
    # Doesn't work yet, gives an weird error
    # def play_track(self, widget):
    #     playsound('sounds/1.mp3')


def main():
    return Soundboardforandroid()
