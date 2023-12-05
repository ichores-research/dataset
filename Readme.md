# iChores Dataset

This set of tools collects data from cameras and microphone and stores them in rosbags.

## Starting the devices

In terminal:

1. Go to the directory of the project
2. Run `./bringup.sh`
3. Make sure everything works, and you can see picture from all the cameras in RViz

## Recording session

In terminal:

1. Go to the directory of the project
2. Run `./record.sh`
3. When finished, press ctrl+C to stop recording
4. Collect the recording from the Documents folder


## Prerequisites

1. Install `ros-noetic-realsense2-camera`
2. Install `ros-noetic-libuvc-camera`
3. Set permissions for the Elgato cameras as shown below
4. Re-connect all Elgato cameras

### UDEV rules for Elgato Cameras

```
# /etc/udev/rules.d/99-uvc.rules
# UVC cameras
SUBSYSTEMS=="usb", ENV{DEVTYPE}=="usb_device", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0078", MODE="0666"

```