import signal
import subprocess
from tkinter import *
import roslaunch


class DatasetApp:
    def __init__(self, parent):
        self.parent = parent
        self.container = Frame(parent)
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
            self._bringup_process = subprocess.Popen("./bringup.sh")
        else:
            print("Shutdown!")
            self._working = False
            self.bringup_button.configure(text="Bringup")
            self._bringup_process.send_signal(signal.SIGINT)
            self._bringup_process = None

    def on_record_click(self):
        if not self._recording:
            print("Record!")
            self._recording = True
            self.record_button.configure(text="Stop")
            package = 'dataset'
            executable = 'record'
            node = roslaunch.core.Node(package, executable)
        else:
            print("Stop!")
            self._recording = False
            self.record_button.configure(text="Record")
            self._recording_process.send_signal(signal.SIGINT)
            self._recording_process.kill()
            self._recording_process = None


root = Tk()
myapp = DatasetApp(root)
root.mainloop()
