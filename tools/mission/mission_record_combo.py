import json
from pynput import keyboard
import time
import threading
import os

defaults = {
    'up': 'w',
    'down': 's',
    'left': 'a',
    'right': 'd',
    'button_a': 'j',
    'button_b': 'k',
    'button_c': 'l',
    'button_d': ';',
    'reset': 'p',
    'exit': 'esc'
}
keybinds = "keybinds.json"

def load_keys():
    if os.path.exists(keybinds):
        with open(keybinds, 'r') as f:
            return json.load(f)
    return defaults

def save_keys(keybindings):
    with open(keybinds, 'w') as f:
        json.dump(keybindings, f)

def mappy(pressed_keys, keybindings):
    stick_map = {
        frozenset(): '5',
        frozenset([keybindings['up']]): '8',
        frozenset([keybindings['left']]): '4',
        frozenset([keybindings['down']]): '2',
        frozenset([keybindings['right']]): '6',
        frozenset([keybindings['up'], keybindings['left']]): '7',
        frozenset([keybindings['up'], keybindings['right']]): '9',
        frozenset([keybindings['down'], keybindings['left']]): '1',
        frozenset([keybindings['down'], keybindings['right']]): '3',
    }
    
    button_map = {
        keybindings['button_a']: 'A',
        keybindings['button_b']: 'B',
        keybindings['button_c']: 'C',
        keybindings['button_d']: 'D'
    }
    
    stick = stick_map.get(frozenset(pressed_keys), '5')  # no keys
    buttons = ''.join(sorted(button_map[k] for k in pressed_keys.intersection(button_map.keys()))) # ok to leave empty
    return stick + buttons

class InputRecorder:
    def __init__(self, keybindings):
        self.keybindings = keybindings
        self.pressed_keys = set()
        self.current_inputs = []
        self.session_count = 0
        self.recording = True
        self.lock = threading.Lock()

    def on_press(self, key):
        try:
            with self.lock:
                if hasattr(key, 'char') and key.char in self.keybindings.values():
                    self.pressed_keys.add(key.char)
                    #print(f"Key pressed: {key.char}")  # Debugging print
                if key == keyboard.KeyCode.from_char(self.keybindings['reset']):
                    self.save_and_reset()
                    print(f"Recording new Combo")
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            with self.lock:
                if hasattr(key, 'char') and key.char in self.pressed_keys:
                    self.pressed_keys.remove(key.char)
        except AttributeError:
            pass

        if key == keyboard.Key.esc:
            self.recording = False
            return False

    def save_and_reset(self):
        if self.current_inputs:
            self.session_count += 1
            filename = f"missioncombo_{self.session_count}.txt"
            
            while os.path.exists(filename):
                self.session_count += 1
                filename = f"recorded_inputs_{self.session_count}.txt"
                
            with open(filename, 'w') as f:
                for input in self.current_inputs:
                    f.write(input + '\n')
            print(f"Inputs saved to {filename}")
            
        else:
            print("No inputs to save.")
        self.current_inputs = []

    def record_loop(self):
        last_record_time = time.time()
        recording_interval = 1/60

        while self.recording:
            current_time = time.time()
            if current_time - last_record_time >= recording_interval:
                with self.lock:
                    current_input = mappy(self.pressed_keys, self.keybindings)
                    self.current_inputs.append(current_input)
                    # print(f"{current_input}")  # if u wanna see it smoooooth
                last_record_time = current_time
            time.sleep(0.001)  # reduce CPU usage?

        self.save_and_reset()

def configgy():
    print("configure buttons - for best results, avoid awkward system inputs like Backspace")
    keybindings = load_keys()

    for action, default_key in keybindings.items():
        new_key = input(f"{action.replace('_', ' ').title()} (current: {default_key}): ") or default_key
        keybindings[action] = new_key

    save_keys(keybindings)
    print("keybinds saved.")

def main():
    print("UNI2 Mission Combo Recipe Recorder (or other FB games i guess)\n")
    print("This will record your inputs in the background, so you can go")
    print("ahead and use this in training mode. Set your buttons the same")
    print("as they are in-game so you can record and reset combos easily.\n")
    print("Press 1 or 2 and hit Enter:")
    print("    (1) Start Combo Recording")
    print("    (2) Configure Keybinds")
    choice = input("")

    if choice == '2':
        configgy()

    keybindings = load_keys()
    recorder = InputRecorder(keybindings)
    
    listener = keyboard.Listener(
        on_press=recorder.on_press,
        on_release=recorder.on_release)
    listener.start()

    record_thread = threading.Thread(target=recorder.record_loop)
    record_thread.start()

    print("Recording inputs. Press 'Esc' to halt.")
    print(f"{keybindings['reset'].upper()} to reset replay recording.")

    listener.join()  # Wait for the listener to stop
    record_thread.join()  # Wait for the recording thread to finish

if __name__ == "__main__":
    main()
