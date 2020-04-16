##
# Print "Pressed up arrow" or "Pressed down arrow" to console when the appropriate key is pressed.
# Using pynput
#
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.up:
        print("Pressed up arrow")
    elif key == keyboard.Key.down:
        print("Pressed down arrow")
    elif key == keyboard.KeyCode.from_char('q'):
        return False


listener = keyboard.Listener(on_press=on_press)
with listener:
    listener.join()
