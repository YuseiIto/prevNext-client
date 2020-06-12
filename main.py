import time
import keyboard
keyboard.press_and_release('shift+s, space')
keyboard.write('The quick brown fox jumps over the lazy dog.')

while True:
    keyboard.send('enter')
    print("Change LIne!")
    time.sleep(0.8)

# Block forever, like `while True`.
keyboard.wait()
