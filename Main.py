import sqlite3
from Student import Student
from MenuOptions import MenuOptions

def ShowOptions():
    print("Here are the different options you can choose from:")
    print("1. Display Students and Attributes")
    print("2. Add a Student")
    print("3. Update a Student")
    print("4. Delete a Student with an ID")
    print("5. Search/Display Students\n")


#main
conn = sqlite3.connect("StudentDB.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Student(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName varchar(25),"
  "LastName varchar(25),GPA NUMERIC,Major varchar(20),FacultyAdvisor varchar(25));")

conn.commit()

menu = MenuOptions()
loop = True
ShowOptions()
while(loop):
    try:
        choose = int(input("Enter a number between 1 and 5 for the action you would like to perform: "))
        if(choose >= 0 and choose < 6):
            if (choose == 1):
                menu.Display()
            elif (choose == 2):
                menu.CreateStudent()
            elif (choose == 3):
                menu.UpdateStudent()
            elif (choose == 4):
                menu.DeleteStudent()
            elif (choose == 5):
                menu.SearchStudent()
        else:
            print("Number entered is not within range.")
            continue
    except ValueError:
        print("Invalid input.")
        continue

    print()
    cont = input("Enter 'Q' to exit program. Enter anything else to continue: ")
    if(cont.lower() == 'q'):
        loop = False
    else:
        print()
        ShowOptions()





