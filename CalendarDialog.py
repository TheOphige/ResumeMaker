#!/usr/bin/env python

# Written in response to: "How do I create a date picker in tkinter?"
# from https://stackoverflow.com/questions/4443786/how-do-i-create-a-date-picker-in-tkinter/27809821
import tkinter

import ttkcalendar
import tkSimpleDialog


class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

# Demo code:


class CalendarFrame(tkinter.LabelFrame):
    def __init__(self, master):
        tkinter.LabelFrame.__init__(self, master, text="CalendarDialog Demo")

        def getdate():
            cd = CalendarDialog(self)
            result = cd.result
            self.selected_date.set(result.strftime("%m/%d/%Y"))

        self.selected_date = tkinter.StringVar()

        tkinter.Entry(self, textvariable=self.selected_date).pack(side=tkinter.LEFT)
        tkinter.Button(self, text="Choose a date", command=getdate).pack(side=tkinter.LEFT)


def main():
    root = tkinter.Tk()
    root.wm_title("CalendarDialog Demo")
    CalendarFrame(root).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
