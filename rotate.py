import time
from gpiozero import Button

# Replace these with your GPIO pin connections.
PIN_A = 20
PIN_B = 26

class App():
    """
    Simple example to listen for change of pin A on the encoder, and determine the direction
    of rotation on reading pin B, whether pin B has "fired" before A.
    """
    def __init__(self):
        self.button_a = Button(PIN_A, pull_up=True)
        self.button_b = Button(PIN_B, pull_up=True)
        self.button_a.when_activated=self.pin_a
        
    def pin_a(self, b):
        if not self.button_b.is_pressed:
            print('Up')
        else:
            print('Down')

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
