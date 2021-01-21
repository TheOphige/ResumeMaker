"""my_CalendarDialog creates calender and provide methods of dialoging with the calender.
The Dialog module contains methods that as the name implies helps to dialog with the calender.
The CalenderDialog module contains methods that binds the Dialog module methods to the calendar to create a dialog box that displays a calendar and returns the selected date"""

from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar

class Dialog(Toplevel):
    """The Dialog module contains methods that as the name implies helps to dialog with the calender.
    Sourced from http://effbot.org/tkinterbook/tkinter-dialog-windows.htm"""
    def __init__(self, parent, title = None):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override




class CalendarDialog(Dialog):
    """The CalenderDialog module contains methods that binds the Dialog module methods to the calendar to create a Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = Calendar(master, selectmode='day')
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.get_date()



def test():
    import tkinter as tk
    root = tk.Tk()
    root.wm_title("Demo")
    
    def getdate():
        cd = CalendarDialog(root)
        result = cd.result
        selected_date.set(result)
        
    selected_date = tk.StringVar()
    selected_date.set('None')
    tk.Entry(root, textvariable=selected_date).pack(side=tk.LEFT)
    tk.Button(root, text="Choose a date", command=getdate).pack(side=tk.LEFT)
  
    root.mainloop()

if __name__ == "__main__":
    test()