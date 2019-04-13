import time
from gpiozero import Button

# Replace these with your GPIO pin connections.
# ... 
# ...    [31]  [33]    [35]    [37]    [39]
# ...    ....  gpio13  gpio19  gpio26  gnd
PIN_A = 19
PIN_B = 26
PIN_SELECT = 13

class App():
    """
    Simple example to listen for change of pin A on the encoder, and determine the direction
    of rotation on reading pin B, whether pin B has "fired" before A.
    """
    def __init__(self):
        self.button_a = Button(PIN_A, pull_up=True)
        self.button_b = Button(PIN_B, pull_up=True)
        self.button_a.when_activated=self.pin_a

        # center button. Use button class to debounce
        self.select = Button(PIN_SELECT, pull_up=True)
        self.select.when_pressed = self.selected

    def pin_a(self, b):
        """
        This is called when user rotate the encoder
        """
        if not self.button_b.is_pressed:
            print('Up')
        else:
            print('Down')

    def selected(self):
        """
        This is called when the center button is pressed.
        """
        print('selected')

    def rotation_sequence(self):
        '''
        Not quite figure this out...
        Not used.
        '''
        a_state = self.button_a.is_pressed
        b_state = self.button_b.is_pressed
        r_seq = (a_state ^ b_state) | b_state << 1
        return r_seq

    def go(self):
        # Note that this loop's wait frequency doesn't really matter.
        # We are using events triggered by the raising edge of pin A
        # to read the activity on the encoder.
        while(1):
            time.sleep(0.01)

if __name__ == '__main__':
    app = App()
    app.go()
