## GamePad Emulator on Python2.7
# Gamepad_Emulator

Translates the signals from the controller, to pressing the key of keyboard.

Requirements:
  1. pygame http://www.pygame.org/news
  2. python keyboard https://pypi.python.org/pypi/keyboard
  3. pyautogui (Actualy, this library don't work when game will running, but Py Keyboard working great!)
  
  
Change the KeyList.py to keys, which you want to simuate.

  How it works:
    PyGame get signals from GamePad and collect this signals into array (function get()). 
    Then, function pushVirtualKey(K) return string value of buttons from gamepad, which was pressed.
    And the end - function pushMultiply(keysSend) emulate pressing and unpressing the button with accordingly with data from KeyList.py
  
