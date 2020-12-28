"""
GUI TEST RUNNER
Run by Typing: "python gui_test_runner.py"
(Use Python 3 - There are GUI issues when using Python 2)
"""

import os
import sys
if sys.version_info[0] >= 3:
    from tkinter import Tk, Frame, Button, Label
else:
    from Tkinter import Tk, Frame, Button, Label


class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(root, width=40).pack()
        self.title = Label(frame, text="", fg="black").pack()
        self.title1 = Label(
            frame, text="Run a Test in Chrome:", fg="blue").pack()
        self.run1 = Button(
            frame, command=self.run_1,
            text="Running all robot test",
            fg="green").pack()

        self.end_title = Label(frame, text="", fg="pink").pack()
        self.quit = Button(frame, text="QUIT", command=frame.quit).pack()

    def run_1(self):
        os.system(
            'robot  *.robot')


if __name__ == "__main__":
    root = Tk()
    root.title("Select Test Job To Run")
    root.minsize(500, 420)
    app = App(root)
    root.mainloop()
