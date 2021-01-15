def wrap(func):
   print("___________________________________________________________________\n", func,"\n___________________________________________________________________")
   return wrap

while True:
    print("\t\t\t\t\tWELCOME TO TEAM BRAVO RESUME MAKER.")
    print("\nTake a look at an example input for personal information")
    print("\nName: Last name First name Middle name\nAddress: 14, ororo street, akoo.\nCity and State: ilorin, Kwara state\nPhone number: 0808763456, 08062727727\nEmail address: koladeleuyo@gmail.com\n")
    print("\nPERSONAL INFORMATION\n")
    name= (input("Enter fullname: ")).upper()
    address= (input("Enter address: ")).title()
    city_state= (input("Enter city and state: ")).title()
    phone_number= input("Enter phone number(at least two most accessible): ") 
    email= input("Enter email(most accessible): ")
    print("These are your inputs")
    print("\n\t\t\t\tPERSONAL INFORMATION")
    pers_info="\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}".format(name,address,city_state,phone_number,email)
    wrap(pers_info)
    #if all the information above is correct input YES otherwise input NO
    next=input("if all the information above is correct input YES otherwise input NO:  ")
    if next.casefold()=="yes":
        break
    elif next.casefold()=="no":
        continue
    else:
        print("I didn't identify your response. So i'm going to the next step. Please enter YES or NO next time.")  
        break
    
####################################
while True:
    print("\nEDUCATION BACKGROUND\n")   
#BRAVO Team led by Bing. The task on educational background submitted by Statesman
    def education_data():
        #print("EDUCATIONAL BACKGROUND")
        deg =  (input("Degree/Certificate Type: ")).title()
        School = (input("Name of School/College: ")).title()
        grade = input("Class of degree: ")
        x = input("Year of graduation (e.g 2036): ")
        if type(x) != int and len(x) != 4:
            print("***Invalid year")   # this is to ensure valid year is entered
            x = input("Year of graduation (e.g 2036): ")
        else:
            print("\n")        # This is to separate the next school info from the previous.        
        more = input("Did you attend another school? (YES / NO): ")  # this is to allow enterance of multiple school information        
        if len(more) >= 3:
            print(education_data())
        else:
            print(" ")  
        edu_bg="\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}".format(deg,School,grade,x)
        wrap(edu_bg)          
    cont = input("Do you have education background? (YES / NO): ") # This will loop education background to allow multiple sch info.
    while len(cont) >= 3:
        print(education_data())
        break        
    #if all the information above is correct input YES otherwise input NO
    next2=input("\nif all the information above is correct input YES otherwise input NO:  ")
    if next2.casefold()=="yes":
        break
    elif next2.casefold()=="no":
        continue
    else:
        print("I didn't identify your response. So i'm going to the next step. Please enter YES or NO next time.")  
        break

######################################
while True:    
    print("\nWORK EXPERIENCE\n")
    work_experience= True
    if work_experience:
        position_title=(input(str('Enter position title : '))).title()
        company_name=(input(str('Enter company\'s name : '))).title()
        city=(input(str('Enter city : '))).title()
        state=(input(str('Enter state : '))).title()
        dates=(input(str('Enter dates : '))).title()
    print("These are your inputs")
    print("\n\t\t\t\tWORK EXPERIENCE")
    work_xp="\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}".format(position_title,company_name,city,state,dates)
    wrap(work_xp)
    #if all the information above is correct input YES otherwise input NO
    next3=input("\nif all the information above is correct input YES otherwise input NO:  ")
    if next3.casefold()=="yes":
        break
    elif next3.casefold()=="no":
        continue
    else:
        print("I didn't identify your response. So i'm going to the next step. Please enter YES or NO next time.")  
        break


#####################################
while True:    
    print("\nSKILLS\n")
    Acquired_Skills= True
    if Acquired_Skills:
        name=(input(str('Name the skill acquired : '))).title()
        company=(input(str('Company the skill was acquired from : '))).title()
        year=input('Year : ')
        address=(input("Company's Address : ")).title()
    print("These are your inputs")
    print("\n\t\t\t\tSKILLS")
    skills="\t\t\t{}\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}".format(name,company,year,address)
    wrap(skills)
    #if all the information above is correct input YES otherwise input NO
    next4=input("\nif all the information above is correct input YES otherwise input NO:  ")
    if next4.casefold()=="yes":
        break
    elif next4.casefold()=="no":
        continue
    else:
        print("I didn't identify your response. So i'm going to the next step. Please enter YES or NO next time.")  
        break

######################################
print('\nThis is your Resume\n')

print("\n\t\t\t\tPERSONAL INFORMATION")
print(pers_info)
print('\n____________________________________________________________\n')
print("\n\t\t\t\tEDUCATION BACKGROUND")
print(education_data())
#print(edu_bg)
print('\n____________________________________________________________\n')
print("\n\t\t\t\tWORK EXPERIENCE")
print(work_xp)
print('\n____________________________________________________________\n')
print("\n\t\t\t\tSKILL")
print(skills)