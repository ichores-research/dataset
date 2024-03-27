#!/usr/bin/python3

import signal
import subprocess
from tkinter import *
import roslaunch
import rospy


def launch_core():
    uuid = roslaunch.rlutil.get_or_generate_uuid(options_runid=None, options_wait_for_master=False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_files=[], is_core=True)
    launch.start()

    return launch

def launch_node(exec):
    rospy.init_node("dataset", anonymous=True)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [f"./launch/{exec}.launch"])
    launch.start()
    rospy.loginfo("started")

    return launch


class DatasetApp:
    def __init__(self, parent):
        self.parent = parent
        self.container = Frame(parent, padx=20, pady=20)
        self.container.pack()

        self.bringup_button = Button(
            self.container, text="Bringup", command=self.on_bringup_click
        )
        self.bringup_button.pack(side=LEFT)
        self.bringup_button.focus_force()

        self.record_button = Button(
            self.container, text="Record", command=self.on_record_click
        )
        self.record_button.pack(side=RIGHT)

        self._working = False
        self._bringup_process = None

        self._recording = False
        self._recording_process = None

    def on_bringup_click(self):
        if not self._working:
            print("Bringup!")
            self._working = True
            self.bringup_button.configure(text="Shutdown")
            self._bringup_process = launch_node("bringup")
            # self._bringup_process = subprocess.Popen("./bringup.sh")
        else:
            print("Shutdown!")
            self._working = False
            self.bringup_button.configure(text="Bringup")
            self._bringup_process.shutdown()
            self._bringup_process = None

    def on_record_click(self):
        if not self._recording:
            print("Record!")
            self._recording = True
            self.record_button.configure(text="Stop")
            self._recording_process = self._bringup_process = launch_node("record")
        else:
            print("Stop!")
            self._recording = False
            self.record_button.configure(text="Record")
            self._recording_process.shutdown()
            self._recording_process = None

core = launch_core()

def on_close():
    core.shutdown()


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_close)
myapp = DatasetApp(root)
root.mainloop()
