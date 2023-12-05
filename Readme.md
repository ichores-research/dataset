

## UDEV rules for Elgato Cameras

```
# /etc/udev/rules.d/99-uvc.rules
# UVC cameras
SUBSYSTEMS=="usb", ENV{DEVTYPE}=="usb_device", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0078", MODE="0666"

```