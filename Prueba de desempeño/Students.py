from Functions import * #import all functions in Functions.py (def)

option=True

def menu(): #The menu for the main archive
    print(""" ---STUDENTS MANAGMENT---
    1. Register a new student.
    2. check the students list.
    3. Search any student
    4. Update students
    5. Delete student
        """)
   
while option != 6: # != is all even 6 

    menu()    
    print("-----------------------------------")
    try: # A try except for error handling
        option =int(input("Select any option \n>> "))
        if option not in range(1,7):
            raise ValueError
    except ValueError:
        print("Please insert a valid option. \n")
        continue 

    if option == 1: #Option to register students
        name = input("Student name: \n>> ")
        id = int(input("Student id \n>> "))
        grade = int(input("Student grade: \n>> "))
        state = input("Student state \n>> ")
        Register_students(name, id, grade, state)
    elif option == 2: # The view of the student list
        Student_list(students)
    elif option == 3: # Student search with specific value ig (Incomplete...)
        Search_students(students)
    elif option == 4:
       pass
    elif option == 5:
        pass
    elif option == 6: # The option to exit the program
        print("Cya...")
    
 