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

- advertasing for connection: blinking every second in the battery charge status colour (:green_circle: more then 80% or charged, :orange_circle: between 20-80%, :red_circle: less then 20%). Set `'advertising_battery_led': False` in _config.py_ to blink :large_blue_circle: instead
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

3. Add the CircuitPython libraries. Download the bundle that matches your CircuitPython version (e.g. **10.x**) from the [official libraries](https://circuitpython.org/libraries) page and unzip it. Copy these folders from the bundle's _lib_ folder into the _/lib_ folder on the CIRCUITPY drive (create it if missing):

- /adafruit_ble
- /adafruit_hid
- /adafruit_lsm6ds
- /adafruit_register
- /adafruit_bus_device

  > **Note**: The libraries are not stored in this repository. Always take them from the bundle that matches your CircuitPython version, otherwise they may not load.

4. Copy _seeed_xiao_nrf52840.py_ from this repository directly onto the CIRCUITPY drive. It controls the battery charging current. A newer version may be available on [PyPI](https://pypi.org/project/circuitpython-seeed-xiao-nrf52840/).

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

## Updating an existing ring

Use these steps to move a ring from an older CircuitPython (e.g. 9.x) to 10.3.1 or newer and install the latest code. Repeat them for each ring.

1. Prepare
   - Download this repository: **Code → Download ZIP**, then unzip it.
   - In Windows remove the ring: _Settings → Bluetooth & devices →_ the ring _→ Remove device_. This clears the old pairing keys.

2. Back up the ring
   - Connect the ring by USB. The **CIRCUITPY** drive appears.
   - Copy everything from it to a folder on your PC.
   - Open _boot_out.txt_ and note the **Board ID** (e.g. `seeed_xiao_nrf52840_sense`).

3. Update the firmware
   - On [circuitpython.org/downloads](https://circuitpython.org/downloads) open the board matching your Board ID and download the latest **stable** _.uf2_ file (10.3.1 or newer, not alpha or beta).
   - Quickly press the reset button twice. A boot drive (e.g. `XIAO-SENSE`) appears.
   - Copy the _.uf2_ file onto it. The ring restarts and **CIRCUITPY** comes back.
   - Check that _boot_out.txt_ shows the new version.

   > **Note**: Files on CIRCUITPY normally survive a firmware update. The backup is there in case they don't.

4. Update the libraries. Libraries must match the CircuitPython major version, so the 9.x ones must be replaced.
   - On [circuitpython.org/libraries](https://circuitpython.org/libraries) download the bundle for your version (e.g. **10.x**) and unzip it.
   - On CIRCUITPY delete the old _lib_ folder and create a new, empty _lib_ folder.
   - From the bundle's _lib_ folder copy these folders into it:
     - /adafruit_ble
     - /adafruit_hid
     - /adafruit_lsm6ds
     - /adafruit_register
     - /adafruit_bus_device

   > **Note**: Do not reuse library files from an older ring or an older copy of this project. They are built for an older CircuitPython and may not load.

5. Copy the new code from the ZIP onto CIRCUITPY, replacing the old files:
   - _code.py_
   - _seeed_xiao_nrf52840.py_
   - _left_config.py_ renamed to _config.py_ for the left ring, or _right_config.py_ renamed to _config.py_ for the right ring.

   If you changed your old _config.py_ (name, pins, `mouse_movement`, ...), make the same changes in the new one. Your backup has the old file.

6. (Optional) Erase the old pairing data on the ring for a clean start
   - Open [Thonny](https://thonny.org/) and choose the **CircuitPython** interpreter (bottom-right corner).
   - Press **Stop**, then type in the Shell:
     ```python
     import _bleio
     _bleio.adapter.erase_bonding()
     ```
   - Close Thonny.

7. Pair again
   - Unplug USB. The LED blinks every second in the battery colour while waiting for a connection.
   - In Windows: _Add device → Bluetooth_ and choose the ring.
   - The blue LED stays on for a few seconds while the connection is secured, then the buttons work.

If something goes wrong:

- **No blinking:** open Thonny and read the error in the Shell. `ImportError` means a library is missing, so copy it from the bundle.
- **3 red blinks after connecting:** remove the ring in Windows and pair once more.
- **To go back:** flash the old _.uf2_ the same way and restore your backup.

## Troubleshooting

### Ring is connected but buttons do nothing

The mouse buttons only work over an encrypted (paired) Bluetooth link. If the computer and the ring disagree about their pairing keys, Windows shows the ring as connected but ignores its buttons.

The ring now checks this after every connection. If the link is not encrypted within a few seconds it asks the computer to pair, and if that fails it blinks :red_circle: 3 times, disconnects and advertises again so the computer can reconnect cleanly.

If the 3 red blinks keep repeating:

1. Remove the ring in Windows Bluetooth settings and pair it again.
2. Make sure the ring runs CircuitPython 10.3.1 or newer (see _boot_out.txt_), with libraries from the matching bundle.
3. To see what happens, connect the ring by USB and open the serial console (e.g. with [Mu](https://codewith.mu/) or [Thonny](https://thonny.org/)). Messages such as `Link not encrypted, requesting pairing` show each step.
