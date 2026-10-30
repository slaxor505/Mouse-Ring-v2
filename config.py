# config.py
# Settings here will override any defaults in code.py
import board
config = {
    'name': 'Left Mouse Ring',
    'left_btn': board.D10,
    'right_btn': board.D8,
    'scrollup_btn': board.D7,
    'scrolldown_btn': board.D9,
    'power_btn': board.D6,
    'mouse_movement': False,        # True - mouse movement & left click; False - mouse buttons & scroll
    'deep_sleep_by_click': True,    # True - activate Deep Sleep by holding buttons for 10 seconds. Valid only when mouse_movement is False
    'advertising_battery_led': True,  # True - blink battery level colour while waiting for connection; False - blink blue
}