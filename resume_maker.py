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

###################################################################################
# personal information

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

###################################################################################
# Education background

# Basic information labelframe
basic_info_label=ttk.Labelframe(e_background, text=' Basic information ')
basic_info_label.grid(column=0, columnspan=4, sticky='W',padx=8, pady=4)
#Degree/Certificate Type
ttk.Label(basic_info_label, text='Degree/ certificate Type:').grid(column=0, row=0)
degree_type= tk.StringVar()
degree_type_entered= ttk.Entry(basic_info_label, width=20, textvariable= degree_type)
degree_type_entered.grid(column=2, row=0, padx=8, pady=4)

# Name of school/college
ttk.Label(basic_info_label, text='Name of school/college:').grid(column=3, row=0)
school_name= tk.StringVar()
school_name_entered= ttk.Entry(basic_info_label, width=20, textvariable= school_name)
school_name_entered.grid(column=4, row=0, padx=8, pady=4)

# Grade labelframe
grade_label=ttk.Labelframe(e_background, text=' Grade ')
grade_label.grid(column=0, row= 1, sticky='W',columnspan=4, padx=8, pady=4)
# current Grade
ttk.Label(grade_label, text='Current Grade:').grid(column=0, row=0)
grade= tk.StringVar()
grade_entered= ttk.Entry(grade_label, width=20, textvariable= grade)
grade_entered.grid(column=1, row=0, padx=8, pady=4)
# Grade scale
ttk.Label(grade_label, text='Grade scale:').grid(column=2, row=0)
grade_scale= tk.StringVar()
grade_scale_entered= ttk.Entry(grade_label, width=20, textvariable=grade_scale)
grade_scale_entered.grid(column=3, row=0, padx=8, pady=4)
# Dates labelframe
Dates_label=ttk.Labelframe(e_background, text=' Dates ')
Dates_label.grid(column=0, row=2, sticky='W', columnspan=4, padx=8, pady=4)
# Year of entry

# Year of graduation

###################################################################################
# Work experience
# company labelframe
company_label=ttk.Labelframe(w_experience, text=' Company Info ')
company_label.grid(column=0, sticky='W', columnspan=4, padx=8, pady=4)
# Company name
ttk.Label(company_label, text='Degree/ certificate Type:').grid(column=0, row=2)
phone_no= tk.StringVar()
phone_no_entered= ttk.Entry(company_label, width=20, textvariable= phone_no)
phone_no_entered.grid(column=1, row=2, padx=8, pady=4)
# Position title
ttk.Label(company_label, text='Name of school/college:').grid(column=2, row=2)
school_name= tk.StringVar()
school_name_entered= ttk.Entry(company_label, width=20, textvariable= email)
school_name_entered.grid(column=3, row=2, padx=8, pady=4)
# location labelframe
location_label=ttk.Labelframe(w_experience, text=' Location ')
location_label.grid(column=0, sticky='W', columnspan=4, padx=8, pady=4)
# country
ttk.Label(location_label, text='Country:').grid(column=0, row=0)
country= tk.StringVar()
country_entered= ttk.Entry(location_label, width=20, textvariable= country)
country_entered.grid(column=1, row=0, padx=8, pady=4)
# city
ttk.Label(location_label, text='City:').grid(column=2, row=0)
city= tk.StringVar()
city_entered= ttk.Entry(location_label, width=20, textvariable= city)
city_entered.grid(column=3, row=0, padx=8, pady=4)
# state
ttk.Label(location_label, text='State:').grid(column=4, row=0)
state= tk.StringVar()
state_entered= ttk.Entry(location_label, width=20, textvariable= state)
state_entered.grid(column=5, row=0, padx=8, pady=4)
# Dates labelframe
Dates_label=ttk.Labelframe(w_experience, text=' Dates ')
Dates_label.grid(column=0, sticky='W', columnspan=4, padx=8, pady=4)
# Year of entry

# Year of leaving


###################################################################################
# skills
# skills labelframe
skills_label=ttk.Labelframe(skills, text=' Skills ')
skills_label.grid(column=0, sticky='W', columnspan=4, padx=8, pady=4)
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






win.mainloop()