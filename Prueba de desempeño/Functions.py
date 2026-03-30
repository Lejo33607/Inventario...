students = [] #List of students

def Register_students(fname, fid, fgrades, fstate):
    """
    Function to register students into the program
    """
    
    fstudent ={
    "name" :  fname,
    "ID" :    fid,
    "grades": fgrades,
    "state" : fstate 
    }
    students.append(fstudent)
    
    for stdent in students:
        print(f"¡Student - {stdent} - Succesfully registered!")
    

def Student_list(students):
    """
    The student list to see who is in
    """
    if not students:
        print("There is no students.")
        return
    
    for student in students:
        print("Students registered: ")
        print(f"{student} \n")

def Search_students(students):
    """
    To search any registered student
    """

    juan=int(input("Insert the id of the student: \n>> ")) #The id in question
    for rstudent in students: # A for to travel to student list
        if rstudent["ID"] == juan:
            return rstudent

def Update_someone():
    pass #Incomplete

def pop_someone(fstudents):
    """
    This function work 'poping' any of the students registered
    """
    students.pop() #incomplete