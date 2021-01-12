import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Resume Maker')
win.iconbitmap('pyc.ico')

tabControl= ttk.Notebook(win)
p_info= ttk.Frame(tabControl)
tabControl.add(p_info, text='Personal Information')
e_background= ttk.Frame(tabControl)
tabControl.add(e_background, text='Education Background')
w_experience= ttk.Frame(tabControl)
tabControl.add(w_experience, text='Work Experience')
skills= ttk.Frame(tabControl)
tabControl.add(skills, text='Skills')
tabControl.pack(expand=5, fill='both', padx=10, pady=6)

# Name label frame
name_label=ttk.Labelframe(p_info, text=' Name ')
name_label.grid(column=0, columnspan=4, padx=8, pady=4)
#first name
ttk.Label(name_label, text='First Name:').grid(column=0, row=0)
firstname= tk.StringVar()
firstname_entered= ttk.Entry(name_label, width=20, textvariable= firstname)
firstname_entered.grid(column=1, row=0, padx=8, pady=4)
#middle name
ttk.Label(name_label, text='Middle Name:').grid(column=2, row=0)
middlename= tk.StringVar()
middlename_entered= ttk.Entry(name_label, width=20, textvariable= middlename)
middlename_entered.grid(column=3, row=0, padx=8, pady=4)
#last name
ttk.Label(name_label, text='Last Name:').grid(column=4, row=0)
lastname= tk.StringVar()
lastname_entered= ttk.Entry(name_label, width=20, textvariable= lastname)
lastname_entered.grid(column=5, row=0, padx=8, pady=4)

# Address label frame
address_label=ttk.Labelframe(p_info, text=' Address ')
address_label.grid(column=0,row=1, columnspan=4, sticky='W', padx=8, pady=4)
#Home address
ttk.Label(address_label, text='Home Address:').grid(column=0, row=1)
home_address= tk.StringVar()
home_address_entered= ttk.Entry(address_label, width=20, textvariable= home_address)
home_address_entered.grid(column=1, row=1, padx=8, pady=4)
#city
ttk.Label(address_label, text='City').grid(column=2, row=1)
city= tk.StringVar()
city_entered= ttk.Entry(address_label, width=20, textvariable= city)
city_entered.grid(column=3, row=1, padx=8, pady=4)
#State
ttk.Label(address_label, text='State:').grid(column=4, row=1)
state= tk.StringVar()
state_entered= ttk.Entry(address_label, width=20, textvariable= state)
state_entered.grid(column=5, row=1, padx=8, pady=4)

# Contacts label frame
contacts_label=ttk.Labelframe(p_info, text=' Contacts ')
contacts_label.grid(column=0, row =2, columnspan=4, sticky='W', padx=8, pady=4)
# Phone number
ttk.Label(contacts_label, text='Phone number:').grid(column=0, row=2)
phone_no= tk.StringVar()
phone_no_entered= ttk.Entry(contacts_label, width=20, textvariable= phone_no)
phone_no_entered.grid(column=1, row=2, padx=8, pady=4)
# Email
ttk.Label(contacts_label, text='Email:').grid(column=2, row=2)
email= tk.StringVar()
email_entered= ttk.Entry(contacts_label, width=20, textvariable= email)
email_entered.grid(column=3, row=2, padx=8, pady=4)
# LinkedIn Id
ttk.Label(contacts_label, text='LinkedIn Id:').grid(column=4, row=2)
linkedin_id= tk.StringVar()
linkedin_id_entered= ttk.Entry(contacts_label, width=20, textvariable= linkedin_id)
linkedin_id_entered.grid(column=5, row=2, padx=8, pady=4)

win.mainloop()