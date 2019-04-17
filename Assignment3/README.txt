Abby Tan
2276413
Partner: Aubrey Fernando
tan177@mail.chapman.edu
Assignment 3

Generating Data:
-ran main.py in Pycharm with Faker to generate 1000 records in Textbook_Exchange.csv

Parsing/Normalizing Data:
-included classes: Main.java, DBconfig.java, & ParseData.java
-DBconfig.java handled connecting to the google cloud DB 
-ParseData.java handled retrieving all the information from the CSV file as
well as importing the data to the DB and normalizing it into smaller tables

Original Table:
Accounts - StudentID, FullName, Email, Password, BookID, BookName, ISBN,
SubjectID, Subject, ClassID, ClassName, Required, TransactionID, TransactionType
	Primary Keys: All the attributes that have ID in it

Tables Made from It:
Books - BookID, BookName, ISBN, Subject, ClassName
Class - ClassID, ClassName, Required
Student - StudentID, FullName, Email, Password
Subjects - SubjectID, Subject 
Transactions - TransactionID, TransactionType