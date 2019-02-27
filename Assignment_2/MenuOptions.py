import sqlite3
from Student import Student

class MenuOptions:

    conn = sqlite3.connect("StudentDB.db")
    cursor = conn.cursor()

    def Display(self):
        MenuOptions.cursor.execute("SELECT * FROM Student")
        result = MenuOptions.cursor.fetchall()
        for x in result:
            print(x)
        MenuOptions.conn.commit()

    def CreateStudent(self):
        while True:
            try:
                first = str(input("Enter student's first name: "))
                last = str(input("Enter student's last name: "))
                gpa = float(input("Enter student's GPA: "))
                major = str(input("Enter student's major: "))
                advisor = str(input("Enter student's faculty advisor: "))
                temp = Student(first, last, gpa, major, advisor)
                MenuOptions.cursor.execute("INSERT INTO Student('FirstName','LastName','GPA','Major','FacultyAdvisor')"
                       "VALUES (?, ?, ?, ?, ?)", temp.getStudentTuple())
                MenuOptions.conn.commit()
                break
            except ValueError:
                print("One of your inputs was an invalid type. Please re-enter all the student information")

    def UpdateStudent(self):
        while True:
            try:
                stu = int(input("Enter the student ID of the student you would like to update: "))
                choice = int(input("Enter 0 if you want to change major, 1 if you want to change advisor, "
                                   "and 2 to change both: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for both the student ID and choice.")

        if choice == 0:
            major = input("Enter updated major: ")
            MenuOptions.cursor.execute("UPDATE Student SET Major = ? WHERE StudentID == ?", (major, stu))
        elif choice == 1:
            advisor = input("Enter updated advisor: ")
            MenuOptions.cursor.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID == ?", (advisor, stu))
        elif choice == 2:
            major = input("Enter updated major: ")
            advisor = input("Enter updated advisor: ")
            MenuOptions.cursor.execute("UPDATE Student SET Major = ? WHERE StudentID == ?", (major, stu))
            MenuOptions.cursor.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID == ?", (advisor, stu))
        else:
            print(choice)
        MenuOptions.conn.commit()


    def DeleteStudent(self):
        while True:
            try:
                stu = input("Enter the student ID of the student you would like to delete: ")
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        MenuOptions.cursor.execute("DELETE FROM Student WHERE StudentID = {0}".format(stu))
        MenuOptions.conn.commit()

    def SearchStudent(self):
        print("Enter 1 for yes and 0 for no.")
        while True:
            try:
                major = int(input("Do you want to search by major? "))
                gpa = int(input("Do you want to search by GPA? "))
                advisor = int(input("Do you want to search by advisor? "))
                break
            except ValueError:
                print("Invalid input for one of the options. Please re-enter your choices.")

        if major == 1:
            searchMaj = input("Enter the major: ")
            MenuOptions.cursor.execute("SELECT * FROM Student WHERE Major == '{0}'".format(searchMaj))
            result = MenuOptions.cursor.fetchall()
            if result != []:
                for x in result:
                    print(x)
        while True:
            try:
                if gpa == 1:
                    searchGpa = input("Enter the GPA: ")
                    MenuOptions.cursor.execute("SELECT * FROM Student WHERE GPA == '{0}'".format(searchGpa))
                    result = MenuOptions.cursor.fetchall()
                    if result != []:
                        for x in result:
                            print(x)
                    break
            except ValueError:
                print("Invalid input for GPA. Please re-enter GPA.")
        if advisor == 1:
            searchAd = input("Enter the faculty advisor: ")
            MenuOptions.cursor.execute("SELECT * FROM Student WHERE FacultyAdvisor == '{0}'".format(searchAd))
            result = MenuOptions.cursor.fetchall()
            if result != []:
                for x in result:
                    print(x)



    def Print(result):
        for x in result:
            print(x)
