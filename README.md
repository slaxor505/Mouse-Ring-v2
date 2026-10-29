# Mouse Ring v2 (joystick)

## Description

![Rings](/images/rings.png)

HID controller with joystick (4 ways and push). There are two functionalities to choose:

- left mouse click, right mouse click, wheel up and wheel down as joystick axis and push to recover from deep sleep
- joystick as mouse movement and left click by push

Built on the basis of the "[Seeed Studio XIAO nRF52840](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html)" microcontroller and programmed in CircuitPython. Controller connects with PC by Bluetooth.

The code was created for the need of easy mouse control with a VR headset. Microcontroller is a core part of Ring made of according the [instruction](https://www.instructables.com/Mouse-Ring-V2/). It's updated version of [original one](https://www.instructables.com/Ring-With-Mouse-Buttons-Wheel/).

## Usability

1. Joystick operations

- as mouse clicks only:

  ![Clicks only](/images/clicks.png)

- as pointer movement:

  ![Movement](/images/movements.png)

  > **Note**: as the _push button_ is occupied by the _left mouse click_, waking up from _deep sleep_ is only possible via the _reset button_.

Of course, different configurations are possible for the Left and right Ring.

2. LEDs communication

- advertasing for connection: :large_blue_circle: blinking every second
- securing the connection (pairing / encryption): :large_blue_circle: continuous light for a few seconds after connecting
- connection could not be secured: :red_circle: 3 fast blinks, then the ring disconnects and advertises again (see [Troubleshooting](#troubleshooting))
- when connected (alternating at approximately every 5 seconds)
  - bluetooth connection confirmation: :large_blue_circle: blink
  - battery charge status: :green_circle: blink - more then 80%, :orange_circle: blink - between 20-80%, :red_circle: blink - less then 20%
- deep sleep: activation of the mode is signaled by fast, one-by-one blinks :red_circle: :green_circle: :large_blue_circle:
- battery charging is indicated by :green_circle: continuous light

3. Battery charge indication:

   ![Charge indication](/images/charge.png)

4. Deep Sleep mode for energy saving can be activated in two ways:

- by long press (around 10 seconds) left or right clicks
- automatically after about 15 minutes of inactivity

Waking up occurs by clicking the joystick.

## Pre-work with the microcontroller

1. Download CircuitPython .uf2 dedicated boot loader from [here](https://circuitpython.org/board/Seeed_XIAO_nRF52840_Sense/).
   Use **CircuitPython 10.3.1 or newer**: it fixes nRF52840 Bluetooth bonding bugs that can leave the ring connected with non-working buttons. Your current version is shown in _boot_out.txt_ on the CIRCUITPY drive.
2. Installing CircuitPython on the microcontroller according the [instruction](https://learn.adafruit.com/welcome-to-circuitpython).
   Simplifying: is needed to reset and enter "boot" mode by quickly pressing the "Reset" button twice.

   ![Seeed Xiao nRF52840](/images/xiao_nRF52840.png)

   Then copy the .uf2 file to the device. The microcontroller will reset automatically.

3. Add selected CircuitPython library files. Can be download from the [official libraries](https://circuitpython.org/libraries) on the CircuitPython website. Required libriaries are:

- /adafruit_ble
- /adafruit_ble_adafruit
- /adafruit_bluefruit_connect
- /adafruit_bus_device
- /adafruit_hid
- /adafruit_lsm6ds
- /adafruit_register
- adafruit_debouncer.mpy
- adafruit_ticks.mpy
- simpleio.mpy

  Unzip downloaded library file and copy required files onto the CIRCUITPY drive into the /lib directory.

  > **Note**: The libraries are included in the release files but may be out of date. libraries version should be the same as boot loader. If you don't care about the latest versions, you can skip this step.

4. To have control with battery charging current download the latest version of _[seeed_xiao_nrf52840.py](https://pypi.org/project/circuitpython-seeed-xiao-nrf52840/)_ or take it from release and place directly on the CIRCUITPY drive.

   > **Note**: _seeed_xiao_nrf52840.py_ is included in the release files but may be out of date. If you don't care about the latest versions, you can skip this step.

## Programming the microcontroller

1. Setting the operation mode in _left_config.py_ and _right_config.py_.

- to work as mouse clicks:
  ```python
    'mouse_movement': False,
  ```
- to work as pointer movement mode:
  ```python
    'mouse_movement': True,
  ```

2. Upload _config.py_

   Copy the files _right_config.py_, _left_config.py_ and _code.py_ onto both devices directly, then:

- for the right controller change file name _right_config.py_ to the _config.py_. File _left_config.py_ can be deleted.
- for the left controller change file name _left_config.py_ to _config.py_. File _right_config.py_ can be deleted.

Correct files structure on the CIRCUITPY:

![Files](/images/files.png)

Reconnect device. Will be visible for Bluetooth and ready to connect.

## Troubleshooting

### Ring is connected but buttons do nothing

The mouse buttons only work over an encrypted (paired) Bluetooth link. If the computer and the ring disagree about their pairing keys, Windows shows the ring as connected but ignores its buttons.

The ring now checks this after every connection. If the link is not encrypted within a few seconds it asks the computer to pair, and if that fails it blinks :red_circle: 3 times, disconnects and advertises again so the computer can reconnect cleanly.

If the 3 red blinks keep repeating:

1. Remove the ring in Windows Bluetooth settings and pair it again.
2. Make sure the ring runs CircuitPython 10.3.1 or newer (see _boot_out.txt_), with libraries from the matching bundle.
3. To see what happens, connect the ring by USB and open the serial console (e.g. with [Mu](https://codewith.mu/) or [Thonny](https://thonny.org/)). Messages such as `Link not encrypted, requesting pairing` show each step.
