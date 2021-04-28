"""This program is a database that holds information similar to the functions of the corona virus tracking app. It has
a new user signup function, a client info search option and an client app function. Encryption keeps the data safe."""

import random
import turtle
import datetime
#import bluetooth  # Needs to be downloaded not in existing library (pip pybluez)
from tkinter import *
from tkinter import ttk
import webbrowser


def setup():
    list_of_students = []
    student_list = open("Student list.txt", 'r')
    for student in student_list:  # Data from file into lists
        list_of_students.append(student)
    for element in range(len(list_of_students)):
        # List_of_students remove tab\t and space\n. Students are placed in linked list[]
        list_of_students[element] = list_of_students[element].replace('\n', '')
        list_of_students[element] = list_of_students[element].split('\t')
    return list_of_students


def hash_setup():
    hash_list = []  # Creates Hash table
    for i in range(30):  # Hash table has 30 elements
        hash_list.append([])
    return hash_list


def append_lists(lists):  # Input data from sheet into hash table
    for students in lists:  # Hash table algorithm
        insert_hash(students)


# End of setup program. These methods create the environment for the App and wouldn't be in the final product.


def insert_hash(students):  # Inserts data into hash table
    word = students[1] + students[3]
    id = appnumber(students[0], hash_element(word))
    try:  # If list is being appended into Hash table method is not called, but if new user is added method is called.
        return_userID(students, id)
    except:
        pass
    students.insert(0, id)
    if len(hash_table[hash_element(word)]) == 0:  # If list is empty add first element
        hash_table[hash_element(word)].append(students)
    if int(students[1]) < int(hash_table[hash_element(word)][0][1]):
        # If element is smaller than the first element insert at[0]
        hash_table[hash_element(word)].insert(0, students)
    if int(students[1]) > int(hash_table[hash_element(word)][-1][1]):
        # If element is larger than the last element in the list
        hash_table[hash_element(word)].append(students)  # Append element at back of list
    else:
        for element in range(1, len(hash_table[hash_element(word)])):
            if int(hash_table[hash_element(word)][element - 1][1]) < int(students[1]) < int(
                    hash_table[hash_element(word)][element][1]):
                # Places entries in ascending order of student number
                hash_table[hash_element(word)].insert(element, students)
                break


def hash_element(word):
    algo = 0
    for letter in word:  # Takes first and last name and creates ord number
        algo = algo + ord(letter)
    location = algo % 30  # Creates location in hash table
    return location


def appnumber(student_id, algo):  # Encryption method create ID code
    algohex = hex(algo * 7 + 16).split('x')[-1]  # Return hex digit without 0x
    studenthex = hex(int(student_id) * 29).split('x')[-1]
    rnd = hex(random.randint(0, 15)).split('x')[-1]  # Random number in code to make description harder
    id = algohex + rnd + studenthex
    end = str(int(id, 16) % 9).split('x')[-1]  # Check digit
    id = id + end
    return str(id)


lists = setup()
global hash_table
hash_table = hash_setup()
append_lists(lists)

print("End of setup \n")


def sec_check():  # Bot check method
    turtlewindow = turtle.Screen()
    turtlewindow.bgcolor("light blue")
    turtlewindow.title("Security check")
    turtlewindow.setup(width=500, height=200)
    turtlewindow.setworldcoordinates(-5000, -2000, 5000, 2000)
    turtlewindow.update()
    bot_turtle = turtle.Turtle()
    bot_turtle.shapesize(0.4, 0.4)
    bot_turtle.shape("circle")
    bot_turtle.color("red")
    turtlewindow.listen()
    turtle.delay(20)

    def clicked(x, y):
        local = bot_turtle.position()
        while dot_itirations < 5:
            if abs(x - local[0]) < 2 and abs(y - local[1]) < 2:
                print('x', abs(x - local[0]), 'y', abs(y - local[1]))
                print('Security check failed \n')
                turtle.bye()
                break
            if abs(x - local[0]) < 100 and abs(y - local[1]) < 100:
                print('x', abs(x - local[0]), 'y', abs(y - local[1]))
                # Print difference between bot_turtle.location and click location
                bot_turtle.lt(random.randint(1, 24) * 15)
                bot_turtle.fd(700)
                security(1)
                break
            else:
                print('Security check failed \n')
                bot_turtle.reset()
                bot_turtle.shapesize(0.4, 0.4)
                return sec_check()
        if dot_itirations == 5:
            turtle.bye()
            print('Security check complete \n')
            return client_signup()

    def security(counter):
        global dot_itirations
        if counter == 0:
            dot_itirations = 0
        else:
            dot_itirations = dot_itirations + counter
        turtlewindow.onscreenclick(clicked)

    security(0)
    turtle.mainloop()
    return
# End of bot check methods


def client_gui():
    global client_window
    client_window = Tk()
    client_window.title("Client Registration")
    client_window.geometry("470x600")
    client_window.config(bg="light green")

    frame1 = Frame(client_window, bg="light green")
    frame1.place(x=50, y=25, width=700, height=530)
    client_window.resizable(False, False)

    Label(frame1, text="CLIENT REGISTRATION", font=("Verdana", 20, "bold"), bg="light green", fg="black").place(x=0, y=10)

    Label(frame1, text="First Name", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=50, y=60)
    global txt_fname
    txt_fname = Entry(frame1, font=("Times New Roman", 15), bg="lightgray")
    txt_fname.place(x=50, y=100, width=250)

    Label(frame1, text="Last Name", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=50, y=140)
    global txt_lname
    txt_lname = Entry(frame1, font=("Times New Roman", 15), bg="lightgray")
    txt_lname.place(x=50, y=180, width=250)
    Label(frame1, text="Title", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=50, y=220)

    global select_title
    select_title = ttk.Combobox(frame1, font=("Arial", 13), state='readonly')
    select_title['values'] = ("MR", "MRS", "MS", "DR", "SIR")
    select_title.place(x=50, y=260, width=250)


    Label(frame1, text="Student Number", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=50, y=300)
    global txt_student_num
    txt_student_num = Entry(frame1, font=("Arial", 15), bg="light gray")
    txt_student_num.place(x=50, y=340, width=250)

    def instructions():
        label = Label(client_window, text="Click on the dot then follow the path and click on the dot again",
                      font=("Arial", 11, "bold"), bg="light green", fg="black")
        label.place(x=0, y=440)

    def do():
        instructions()
        sec_check()
    Checkbutton(frame1, command=do, text="I'm not a robot",bg="light green", font=("Arial", 12)).place(x=50, y=380)
    Label(frame1, text="For additional COVID-19 information click the button below", font=("Arial", 11, "bold"), bg="light green", fg="black").place(x=0, y=450)
    Button(frame1, command=covid_info, text="COVID-19 Information Page", bg="green", font=("Arial", 12, "bold")).place(x=50, y=480)
    client_window.mainloop()


def covid_info():  # Called in client_gui
    webbrowser.open('https://covid19inlanguage.homeaffairs.gov.au/')


def client_signup():  # Client input towards database(name, lastname,title ,student number)
    name = txt_fname.get().replace("'", "\'").upper()
    # \' Force string to avoid code changes by external users.
    lastname = txt_lname.get().replace("'", "\'").upper()  # Replace ' with \' to avoid code exit string
    title = select_title.get().replace("'", "\'").upper()
    stnumber = txt_student_num.get().replace("'", "\'")
    client_window.destroy()
    return new_user([stnumber, lastname, title, name])

def new_user(students):
    # Calls dummy_method(). This step can be skipped. It's just in place to show Student Id authentication by CDU
    dummy_method(students)
    return panel()

def dummy_method(students):  # This method represents details being sent to the CDU database and to check
    # if the information and Student ID is correct it is sent back and then appended in the Hash table by insert hash.
    return insert_hash(students)

def return_userID(user, id):  # Writes a file as output example with code and user detail.
    user, id = str(user), str(id)
    accept_window = Tk()
    accept_window.attributes('-topmost', True)
    accept_window.title("Client Registration")
    accept_window.geometry("250x80")
    accept_window.config(background="light green")
    accept_frame = Frame(accept_window)
    accept_frame.pack()
    sign_in = Label(accept_frame, text="Sign-up Complete", fg="Black", bg="light green", font="Ariel 12 bold")
    sign_in.pack()
    file = open("New Users Output.txt", 'w')
    file.write(id + user + "\n")
    file.close()

# End of client sign up Methods

def panel():  # Central control panel
    print("Database examples (Only for reference it won't show in final product)")
    print(hash_table[3])  # A chained list of hash table at a specific element
    count = 0
    for i in range(len(hash_table)):
        count = count + len(hash_table[i])
    print("number of elements in table=", count, '\n')
    global panel_window  # Global variable to allow panel.destroy from any method
    panel_window = Tk()
    panel_window.attributes('-topmost', True)
    panel_window.title("Control Panel")
    panel_window.geometry("240x240")
    panel_window.resizable(False, False)  # Prevents the window from being resized.
    panel_window.config(background="light green")

    heading_frame = Frame(panel_window)
    Label(heading_frame, text="Choose Input Type", fg="black", bg="light green",
          font=("Arial", 12, "bold")).pack()
    heading_frame.pack()
    buttons_frame = Frame(panel_window)
    buttons_frame.config(background="light green", bd="5")
    buttons_frame.pack(side=TOP)
    client = Button(buttons_frame, text="Client", fg="green", font="times 12 bold")
    client.bind("<Button-1>", client_panel)
    client.config(height=2, width=20)
    user = Button(buttons_frame, text="User", fg="green", font="times 12 bold")
    user.bind("<Button-1>", user_panel)
    user.config(height=2, width=20)
    app = Button(buttons_frame, text="App", fg="green", font="times 12 bold")
    app.bind("<Button-1>", bluetooth_search)
    app.config(height=2, width=20)
    exit_panel = Button(buttons_frame, text="Quit", fg="green", font="times 12 bold")
    exit_panel.bind("<Button-1>", quit_menu)
    exit_panel.config(height=2, width=20)
    client.pack(side=TOP)
    user.pack(side=TOP)
    app.pack(side=TOP)
    exit_panel.pack(side=BOTTOM)
    panel_window.mainloop()


def user_panel(event):
    panel_window.destroy()
    user_login()


def client_panel(event):
    panel_window.destroy()
    client_gui()


def quit_menu(event):
    panel_window.destroy()
    print("Goodbye")


# End of panel methods


def user_login():
    global login_window
    login_window = Tk()
    login_window.title("User Sign-in")
    login_window.geometry("400x300")
    login_window.config(bg="light green")
    frame1 = Frame(login_window, bg="light green")
    frame1.place(x=50, y=25, width=700, height=500)
    login_window.resizable(False, False)

    Label(frame1, text="USER SIGN-IN", font=("Verdana", 22, "bold"), bg="light green",
          fg="black").place(x=25, y=5)
    Label(frame1, text="Username", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=30, y=50)
    global txt_username
    txt_username = Entry(frame1, font=("Times New Roman", 15), bg="lightgray")
    txt_username.place(x=30, y=90, width=250)

    Label(frame1, text="Password", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=30, y=130)
    global txt_password
    txt_password = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", show="*")
    txt_password.place(x=30, y=170, width=250)

    btn_signin = Button(frame1, command=sign_in, text="Sign-in", font=("Verdana", 10, "bold"),
                        background="green", width=10)
    btn_signin.place(x=30, y=220, width=250)
    login_window.mainloop()

def sign_in():  # Method for user to sign in and check username and password
    user = txt_username.get().upper()
    if txt_username.get() == "conner" and txt_password.get() == "hit137":
        login_window.destroy()
        return user_gui(user+" "+"001")
    else:
        login_window.destroy()
        print("Username and password not accepted \n")
        return panel()

def user_gui(user):
    global search_window
    search_window = Tk()
    search_window.title("Student Search")
    search_window.geometry("1200x575")
    search_window.config(bg="light green")
    frame1 = Frame(search_window, bg="light green")
    frame1.place(x=50, y=25, width=1200, height=700)
    frame2 = Frame(search_window, bg="light green")
    frame2.place(x=100, y=230, width=1200, height=300)
    search_window.resizable(False, False)
    Label(frame1, text="CONTACT TRACING", font=("Verdana", 20, "bold"), bg="light green",
          fg="black").place(x=40, y=5)
    Label(frame1, text=user, font=("Verdana", 20, "bold"), bg="light green", fg="black").place(x=500, y=5)
    Label(frame1, text="Enter ID code", font=("Arial", 15, "bold"), bg="light green",
          fg="black").place(x=50, y=40)
    global txt_idcode
    txt_idcode = Entry(frame1, font=("Times New Roman", 15), bg="lightgray")
    txt_idcode.place(x=50, y=90, width=250)

    btn_submit = Button(frame1, command=user_search, text="Search", font=("Verdana", 10, "bold"), background="green"
                        , width=10)
    btn_submit.place(x=50, y=130, width=250)

    Label(frame1, text="Search Result", font=("Arial", 15, "bold"), bg="light green", fg="black").place(x=50, y=170)
    global search_hist
    search_hist = Listbox(frame2, width=150, font=("Times New Roman", 11), bg="lightgray")
    search_hist.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame2, orient="vertical")
    scrollbar.config(command=search_hist.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    search_hist.config(yscrollcommand=scrollbar.set)
    Button(frame1, command=user_quit, text="Quit", bg="light green",
           font=("Arial", 12, "bold")).place(x=50, y=510)
    search_window.mainloop()

def user_quit():
    search_window.destroy()
    return panel()


def user_search():
    search_code = txt_idcode.get().replace("'", "")
    if len(search_code) == 10:
        return check_digit(search_code)
    else:
        print("Code is incorrect(len(search_code)!=10)")
        search_hist.insert(0, "Code is incorrect(len(search_code)!=10)")


def check_digit(id):  # Run check value against the code to see if valid
    z = str(int(id[0:9], 16) % 9).split('x')[-1]
    if int(id, 16) < 1:  # To check that code is not 0000000000 and pass the check code process
        print("Check digit failed (ID code all 0) \n")
        search_window.destroy()
        return panel()
    if z == id[9]:
        print("Check digit complete")
        return search_algorithm(id, hash_table)
    else:
        print("Check digit failed (Check digit doesn't match code)")
        search_hist.insert(0, "Check digit failed (Check digit doesn't match code)")
    return


def search_algorithm(code, hashtable):
    hashlocal = int((int(code[0:2], 16) - 16) / 7)  # Extract Hash table location from hex to decimal
    studentnumber = int(int(code[3:9], 16) / 29)  # Extract student ID number from hex to decimal
    print("hash table location:", hashlocal, "decrypted student number:", studentnumber)
    binary_search(hashtable[hashlocal], studentnumber, 0, len(hashtable[hashlocal]) - 1, code)


def binary_search(hash_list, studentnumber, start, end,
                  code):  # Using binary search method to reduce search time in large number lists
    middle = (start + end) // 2
    if studentnumber == int(hash_list[middle][1]):
        if code == hash_list[middle][0]:  # Check entree against ID code. if False then code is expired and doesnt
            return found_search(hash_list[middle])  # Return the data
        else:
            print("Data not found. Code is expired or fake 'ID code doesn't match directory'\n")
            search_hist.insert(0, "Data not found. Code is expired or fake 'ID code doesn't match directory")
            return
    if int(hash_list[-1][1]) < studentnumber or int(hash_list[0][1]) > studentnumber or int(
            hash_list[middle - 1][1]) < studentnumber < int(hash_list[middle][1]):
        print("Code not in database\n")
        search_hist.insert(0, "Code not in database")
        # Statement to compensate if the data doesnt exist in the database but the code passed the security checks
        return panel()
    if studentnumber < int(hash_list[middle][1]):
        return binary_search(hash_list, studentnumber, start, middle - 1, code)
    if studentnumber > int(hash_list[middle][1]):
        return binary_search(hash_list, studentnumber, middle + 1, end, code)


def found_search(student_index):
    print('result=', *student_index, '\n')
    search_hist.insert(0, student_index)
    return


# End of user search methods

def bluetooth_search(event):  # Method to show device being detected and code acquired (device name will be code)
    # This is only proof of concept method to show bluetooth broadcast and doesn't contribute
    # to the database. Method can be skipped and will only be used in presentation.
    panel_window.destroy()
    print("Searching for devices...")
    now = datetime.datetime.now()
    #nearby_devices = bluetooth.discover_devices()  # No bluetooth devices will be located so return (none,Fake ID)
    nearby_devices = [("none", "254672f9a3")]  # Code in brackets will pass security checks but wont return Info.
    print("Codes detected")
    for name in nearby_devices:
        print("Code:", name[1], "Date and Time", now.strftime("%m-%d %H:%M"), '\n')
        # Time is recorded because Data should only be kept for 21 days then deleted and aids in Covid tracing
    bluetooth_window = Tk()
    bluetooth_window.attributes('-topmost', True)
    bluetooth_window.title("Tracing App")
    bluetooth_window.geometry("250x80")
    bluetooth_window.config(background="light green")
    frame1 = Frame(bluetooth_window)
    frame1.pack()
    heading = Label(frame1, text="Found Client", fg="Black", bg="light green", font="Ariel 12 bold")
    heading.pack()
    frame2 = Frame(bluetooth_window)
    frame2.config(bd="2", relief=GROOVE)
    date = Label(frame2, text="Date and Time:")
    idcode = Label(frame2, text="ID code:")
    currenttime = Label(frame2, text=now.strftime("%m-%d %H:%M"))
    bluetooth_device = Label(frame2, text=name[1])
    date.grid(row=1, sticky=E, padx=(10, 10))
    idcode.grid(row=2, sticky=E, padx=(10, 10))
    currenttime.grid(row=1, column=1)
    bluetooth_device.grid(row=2, column=1)
    frame2.pack()
    print("Close window to return to panel()\n")
    bluetooth_window.mainloop()
    return panel()


# End of App methods

panel()  # First method called after list is added into hash table.

"""
Errors:
- Client signup can't be used twice due to error on the turtle screen for security check. turtle cant be loaded twice
- During security check if the user clicks on the screen to fast the turtle crashes.
- Dummy method is to symbolise name and student number being checked against the CDU database.
    I do not have access to check it.(Probably a good thing I don't have access). If the student numbers are not 
    correct and not 6 digits then the ID code generated wont work.
Setup:
- A list of students and their student numbers (Student list.txt) is uploaded into the Hash Table Database to show how 
    the data is entered and stored
- For each student a code is generated and returned to them. This code is used to locate the students information and is
    encrypted with several safety checks. The stored code doesn't hold any personal information only the location in 
    list and the Student ID number.
- An example of an element in the hash table is printed to show how the data is stored and give ID codes that the user
    can search.
- 'panel()' GUI will show 4 options Client(Person signing up to the database with their information), User(Person using 
    codes to find the students information), App(showing the bluetooth search method for program) and Quit(exit program)
- In client the client will enter their information(first name, lastname,title,Student ID) these variables are saved 
    with /' replaced so that extra code cant be entered into the system. The system will save the input as a string 
    regardless of input. Student ID is checked to see if input is digit.
- Bot check will activate to make sure it is a person not a bot. A window will appear and the client must click on the 
    dot and the dot will move. After move the client must click on the dot again till the check is complete. if the 
    client misses the dot then it will reset. If the client click and turtle.position() are within 10 px then the 
    security check will fail. Click coordinates cant return turtle.position(). The terminal will print the 5 values 
    which is the difference of the click coordinates and turtle.heading().
_If the bot check is successful the information will be written and saved in a text file in this folder with the ID code
    and will also be sent to a method called dummy_method(). This method represents the information being sent to the 
    CDU servers and being verified and then sent back to the database insert_hash() to be added to the hash table.
- Once the information is added the number of elements in the list will print and it will show 1 extra entry. This 
    proves that the data was entered. 
- User method prompts the User to enter the code that they have received and find out the information of the person 
    who was allocated that code. This shows how codes will be searched for contact tracing. Clients can only be found 
    using codes and not any other search method.
- Once the code is entered the code must pass all security checks first. The first check is the Check_digit and it sees
    if the entered code is valid (The system will not accept 0000000000 as an entered code). Once the Check_digit is 
    passed the program will decrypt the code and search for the client. If the student ID is not in the database it will
    return not found. If the student ID is found in the Hash table element location the ID code entered by the user is 
    checked against the code saved in the system for that client. If the code doesnt match then the information is not
    returned.
- App panel option initialises the bluetooth search of devices in the area. This is proof of concept only and wont 
    work properly. This just shows that information can be searched and received by a bluetooth device. The bluetooth 
    search returns found devices and the date and time. The time is stored and if the information is older than 30 days
    it will be deleted as per Covid tracing laws.
- Quit can be called at any time in the control panel to stop the program


Notes:
- Double entry of exact same details will not be appended into hash table
- Binary search of hash table reduces the search time for every list. In small numbers like this it doesnt have a big
     improvement over linear search but if you have 1 million entries binary worst run time is 20 recursions. To place 
     it into perspective. Linear search of 24 million + output = 2 minutes 29 seconds Binary search of 24 million = 
     1.77*10^-4 seconds. If every entry is searched at least once 24 million^2 lineur will take 59,6 million minutes.
     Binary will take 71 minutes to search 24 million^2 entries.
- Number of elements in the list that appends at the start = 218 if print statement 'number of elements in table=' 
    = to 218 then all elements from the list is added into the Hash table. 
- Generated code ID is 10 hex digit number (259672f9a8). First 2 numbers are the location in the hash table encrypted
    third number is randomly generated by the system to unsure that the code is unique and if the code setup is revealed
    then they cant guess the random number and the check digit numbers 4 to 9 is the student id
    number encrypted and the last number is a check digit. The check digit makes sure that the ID given is generated by
    the system and not a fake random number. When searching check digit must pass first before search is initiated.
- When User enters a code it must pass the check digit first before the code is accepted.
- If user enters a code previously generated by the system and can pass the security checks and the student number is 
    located, but the index entry and the search code doesn't match then it doesnt return the information just 
    'Data not found. Code is expired or fake'
- If the user enters a code that passes the security system but the entry student number doesn't exist, then the system
    returns 'Code not in database' 
- If the user enters the code 0000000000 then this code would technically pass the security checks but an extra check 
    is in place to avoid this. if int of the generated code == 0 then search fails at check digit()
"""
