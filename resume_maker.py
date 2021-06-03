import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, Spinbox, filedialog as fd, messagebox as mBox 
from my_CalendarDialog import CalendarDialog 
import location_helper as lh
import ToolTip as tt

# Creating a Window ===========================================================
win = tk.Tk()
win.title('Resume Maker')
win.iconbitmap('pyc.ico')

# Creating tabs ===============================================================
tabControl= ttk.Notebook(win)
p_info= ttk.Frame(tabControl)
tabControl.add(p_info, text='Personal Information')
e_background= ttk.Frame(tabControl)
tabControl.add(e_background, text='Education Background')
w_experience= ttk.Frame(tabControl)
tabControl.add(w_experience, text='Work Experience')
skills= ttk.Frame(tabControl)
tabControl.add(skills, text='Skills')
tabControl.pack(expand=5, fill='both', padx=4, pady=6)

# Creating a Menu Bar ==========================================================
def _quit():
      win.quit()
      win.destroy()
      exit() 
def _msg():
      mBox.showinfo('About: Resume Maker', 'Resume Maker \nWritten by Theophilus Ige')
def help():
      def _quithelp():
            help_win.destroy()
      
      help_win= tk.Toplevel(win)
      help_win.title('Help: Resume Maker')
      help_win.iconbitmap('pyc.ico')
      texts= 'This tool can be used to download a variety of corpora and models \nthat can be used with NLTK.  Each corpus or model is distributed \nin a single zip file, known as a "package file."  You can \ndownload packages individually, or you can download pre-defined \ncollections of packages.\n\nWhen you download a package, it will be saved to the "download \ndirectory."  A default download directory is chosen when you run \nthe downloader; but you may also select a different download \ndirectory.  On Windows, the default download directory is \n"package." \n\nThe NLTK downloader can be used to download a variety of corpora, \nmodels, and other data packages. '

      ttk.Label(help_win, text= texts).pack(side=tk.TOP, padx=8, pady=4)
      tk.Button(help_win, text="Ok", command= _quithelp).pack(side=tk.BOTTOM, padx=8, pady=4)

menuBar = Menu(p_info)
win.config(menu=menuBar)
        
# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New           Ctrl-N')
fileMenu.add_separator()
fileMenu.add_command(label='Exit          Ctrl-X', command=_quit)
menuBar.add_cascade(label='File', menu=fileMenu)
        
# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=_msg)
helpMenu.add_command(label='Instructions  F1', command=help)
menuBar.add_cascade(label='Help', menu=helpMenu)
###################################################################################
# personal information

# Name label frame -----------------------------------------------------------------
name_label=ttk.Labelframe(p_info, text=' Name ')
name_label.grid(column=0, columnspan=8,sticky='WE', padx=8, pady=4)
#first name
ttk.Label(name_label, text='First Name:').grid(column=0, row=0, padx=8, pady=4)
firstname= tk.StringVar()
firstname_entered= ttk.Entry(name_label, width=20, textvariable= firstname)
firstname_entered.grid(column=1, row=0, padx=8, pady=4)
tt.create_ToolTip(firstname_entered, 'This is an entry widget.')
#middle name
ttk.Label(name_label, text='Middle Name:').grid(column=2, row=0, padx=8, pady=4)
middlename= tk.StringVar()
middlename_entered= ttk.Entry(name_label, width=20, textvariable= middlename)
middlename_entered.grid(column=3, row=0, padx=8, pady=4)
#last name
ttk.Label(name_label, text='Last Name:').grid(column=4, row=0, padx=8, pady=4)
lastname= tk.StringVar()
lastname_entered= ttk.Entry(name_label, width=20, textvariable= lastname)
lastname_entered.grid(column=5, row=0, padx=8, pady=4)

# Address label frame -----------------------------------------------------------------
address_label=ttk.Labelframe(p_info, text=' Address ')
address_label.grid(column=0,row=1, columnspan=8, sticky='WE', padx=8, pady=4)
#Home address
ttk.Label(address_label, text='Home Address:').grid(column=0, row=1, padx=8, pady=4)
home_address= tk.StringVar()
home_address_entered= ttk.Entry(address_label, width=20, textvariable= home_address)
home_address_entered.grid(column=1, row=1, padx=8, pady=4)
#country
ttk.Label(address_label, text='Country:').grid(column=2, row=1, padx=8, pady=4)
country = ttk.Combobox(address_label, width=12, values = lh.countries)
country.current(0)
country.grid(column=3, row=1, padx=8, pady=4) 
tt.create_ToolTip(country, 'This is a dropdown.')
# country callback 
def onchange(e):
      state.config(value= lh.country_states[country.get()])
      state.current(0)     
# bind country to state
country.bind("<<ComboboxSelected>>", onchange)

#State
ttk.Label(address_label, text='State:').place(x=490,y=0)
state = ttk.Combobox(address_label, width=12, values=[])
state.place(x=540,y=0)      

# Contacts label frame -----------------------------------------------------------------
contacts_label=ttk.Labelframe(p_info, text=' Contacts ')
contacts_label.grid(column=0, row =2, columnspan=8, sticky='WE', padx=8, pady=4)
# Phone number
ttk.Label(contacts_label, text='Phone number:').grid(column=0, row=2, padx=8, pady=4)
phone_no= tk.StringVar()
phone_no_entered= ttk.Entry(contacts_label, width=20, textvariable= phone_no)
phone_no_entered.grid(column=1, row=2, padx=8, pady=4)
# Email
ttk.Label(contacts_label, text='Email:').grid(column=2, row=2, padx=8, pady=4)
email= tk.StringVar()
email_entered= ttk.Entry(contacts_label, width=20, textvariable= email)
email_entered.grid(column=3, row=2, padx=8, pady=4)
# LinkedIn Id
ttk.Label(contacts_label, text='LinkedIn Id:').grid(column=4, row=2, padx=8, pady=4)
linkedin_id= tk.StringVar()
linkedin_id_entered= ttk.Entry(contacts_label, width=20, textvariable= linkedin_id)
linkedin_id_entered.grid(column=5, row=2, padx=8, pady=4)

# preview skills
p_info_preview= tk.Button(p_info, text="Preview")
p_info_preview.grid(column=3,row=4, sticky='WE',padx=8, pady=4)
###################################################################################
# Education background

# Basic information labelframe -----------------------------------------------------------------
basic_info_label=ttk.Labelframe(e_background, text=' Basic information ')
basic_info_label.grid(column=0, columnspan=8, sticky='WE',padx=8, pady=4)
#Degree/Certificate Type
ttk.Label(basic_info_label, text='Degree/ certificate Type:').grid(column=0, row=0, padx=8, pady=4)
degree_type= tk.StringVar()
degree_type_entered= ttk.Entry(basic_info_label, width=20, textvariable= degree_type)
degree_type_entered.grid(column=2, row=0, padx=8, pady=4)

# Name of school/college
ttk.Label(basic_info_label, text='Name of school/college:').grid(column=3, row=0, padx=8, pady=4)
school_name= tk.StringVar()
school_name_entered= ttk.Entry(basic_info_label, width=20, textvariable= school_name)
school_name_entered.grid(column=4, row=0, padx=8, pady=4)

# Grade labelframe -----------------------------------------------------------------
grade_label=ttk.Labelframe(e_background, text=' Grade ')
grade_label.grid(column=0, row= 1, sticky='WE',columnspan=8, padx=8, pady=4)
# current Grade
ttk.Label(grade_label, text='Current Grade:').grid(column=0, row=0, padx=8, pady=4)
grade= tk.StringVar()
grade_entered= ttk.Entry(grade_label, width=20, textvariable= grade)
grade_entered.grid(column=1, row=0, padx=8, pady=4)
# Grade scale
ttk.Label(grade_label, text='Grade scale:').place(x=360,y=2)
grade_scale= tk.StringVar()
grade_scale_entered= ttk.Entry(grade_label, width=20, textvariable=grade_scale)
grade_scale_entered.place(x=450,y=2)

# Dates labelframe -----------------------------------------------------------------
Dates_label=ttk.Labelframe(e_background, text=' Dates ')
Dates_label.grid(column=0, row=2, sticky='WE', columnspan=8, padx=8, pady=4)
# Year of entry
def getentdate():
    cd = CalendarDialog(Dates_label)
    result = cd.result
    entry_date.set(result)

entry_date_button= tk.Button(Dates_label, text="Choose entry date", command=getentdate)
entry_date_button.pack(side=tk.LEFT, padx=8, pady=4)
tt.create_ToolTip(entry_date_button, 'This is a Date Picker.')
entry_date = tk.StringVar()
entry_date.set('None')
tk.Entry(Dates_label, textvariable=entry_date).pack(side=tk.LEFT, padx=8, pady=4)


# Year of graduation
def getgraddate():
    cd = CalendarDialog(Dates_label)
    result = cd.result
    graduation_date.set(result)

tk.Button(Dates_label, text="Choose graduation date", command=getgraddate).pack(side=tk.LEFT, padx=8, pady=4)
graduation_date = tk.StringVar()
graduation_date.set('None')
tk.Entry(Dates_label, textvariable=graduation_date).pack(side=tk.LEFT, padx=8, pady=4)


# preview Education background
e_background_preview= tk.Button(e_background, text="Preview")
e_background_preview.grid(column=3,row=4,sticky='WE', padx=8, pady=4)
###################################################################################
# Work experience

# company labelframe -----------------------------------------------------------------
company_label=ttk.Labelframe(w_experience, text=' Company Info ')
company_label.grid(column=0, sticky='WE', columnspan=8, padx=8, pady=4)
# Company name
ttk.Label(company_label, text='Degree/ certificate Type:').grid(column=0, row=2, padx=8, pady=4)
phone_no= tk.StringVar()
phone_no_entered= ttk.Entry(company_label, width=20, textvariable= phone_no)
phone_no_entered.grid(column=1, row=2, padx=8, pady=4)
# Position title
ttk.Label(company_label, text='Name of school/college:').grid(column=2, row=2, padx=8, pady=4)
school_name= tk.StringVar()
school_name_entered= ttk.Entry(company_label, width=20, textvariable= email)
school_name_entered.grid(column=3, row=2, padx=8, pady=4)

# location labelframe -----------------------------------------------------------------
location_label=ttk.Labelframe(w_experience, text=' Location ')
location_label.grid(column=0, sticky='WE', columnspan=8, padx=8, pady=4)
# Company address
ttk.Label(location_label, text='company Address:').grid(column=0, row=0, padx=8, pady=4)
company_address= tk.StringVar()
company_address_entered= ttk.Entry(location_label, width=20, textvariable= company_address)
company_address_entered.grid(column=1, row=0, padx=8, pady=4)
# company country
ttk.Label(location_label, text='Country:').grid(column=2, row=0, padx=8, pady=4)
company_country= ttk.Combobox(location_label, width=12, values = lh.countries)
company_country.current(0)
company_country.grid(column=3, row=0, padx=8, pady=4)

# company country callback 
def onchange(e):
      company_state.config(value= lh.country_states[company_country.get()])
      company_state.current(0)     
# bind country to state
company_country.bind("<<ComboboxSelected>>", onchange)

# company state
ttk.Label(location_label, text='State:').grid(column=4, row=0, padx=8, pady=4)
company_state= ttk.Combobox(location_label, width=12, values=[])
company_state.grid(column=5, row=0, padx=8, pady=4)

# Dates labelframe -----------------------------------------------------------------
WDates_label=ttk.Labelframe(w_experience, text=' Dates ')
WDates_label.grid(column=0, sticky='WE', columnspan=8, padx=8, pady=4)

# Year of entry
def getWentdate():
    cd = CalendarDialog(WDates_label)
    result = cd.result
    Wentry_date.set(result)

tk.Button(WDates_label, text="Choose entry date", command=getWentdate).pack(side=tk.LEFT, padx=8, pady=4)
Wentry_date = tk.StringVar()
Wentry_date.set('None')
tk.Entry(WDates_label, textvariable=Wentry_date).pack(side=tk.LEFT, padx=8, pady=4)


# Year of leaving
def getleavedate():
    cd = CalendarDialog(WDates_label)
    result = cd.result
    leaving_date.set(result)

tk.Button(WDates_label, text="Choose leaving date", command=getleavedate).pack(side=tk.LEFT, padx=8, pady=4)
leaving_date = tk.StringVar()
leaving_date.set('None')
tk.Entry(WDates_label, textvariable=leaving_date).pack(side=tk.LEFT, padx=8, pady=4)


# preview work experience
workXP_preview= tk.Button(w_experience, text="Preview")
workXP_preview.grid(column=3,row=4, sticky='WE',padx=8, pady=4)
###################################################################################
# skills

# skills labelframe -----------------------------------------------------------------
skills_label=ttk.Labelframe(skills, text=' Skills ')
skills_label.grid(column=0, sticky='WE', columnspan=8, padx=8, pady=4)
# skill name
ttk.Label(skills_label, text='Skill name:').grid(column=0, row=0)
skill_name= tk.StringVar()
skill_name_entered= ttk.Entry(skills_label, width=20, textvariable= skill_name)
skill_name_entered.grid(column=1, row=0, padx=8, pady=4)
# skill level
ttk.Label(skills_label, text='Skill level(%):').grid(column=3, row=0)
skill_level= tk.StringVar()
skill_level_entered= ttk.Entry(skills_label, width=20, textvariable= skill_level)
skill_level_entered.grid(column=4, row=0, padx=8, pady=4)
# company acquired
ttk.Label(skills_label, text='Company acquired:').grid(column=5, row=0, pady=16)
company_acquired= tk.StringVar()
company_acquired_entered= ttk.Entry(skills_label, width=20, textvariable= company_acquired)
company_acquired_entered.grid(column=6, row=0, padx=8, pady=16)
# preview skills
skills_preview= tk.Button(skills, text="Preview")
skills_preview.grid(column=3,row=4,sticky='WE', padx=8, pady=4)


# preview labelframe -----------------------------------------------------------------
preview_label=ttk.Labelframe(win, text=' Preview ')
preview_label.pack(expand=5, fill='both', padx=4, pady=2)
ttk.Label(preview_label, text='Company acquired:').pack(expand=5, fill='both', padx=8, pady=4)


# Download button
tk.Button(win, text="Download Resume", font=('Helvetica', 16, 'bold'), bg='black', fg='green').pack(expand=5, fill='both', padx=4, pady=2)



win.mainloop()