import sqlite3

class Student:
    def __init__(self, firstName, lastName, gpa, major, facAdvis):
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
        self.major = major
        self.facAdvis = facAdvis

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getGPA(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getFacultyAdvisor(self):
        return self.facAdvis

    def getStudentTuple(self):
        return(self.getFirstName(),self.getLastName(),self.getGPA(),self.getMajor(), self.getFacultyAdvisor())

    def getConn(self):
        conn = sqlite3.connect("StudentDB.db")
        return conn

    def getCursor(self):
        conn = self.getConn()
        cursor = conn.cursor()
        return cursor

