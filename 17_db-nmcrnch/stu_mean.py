#StewMeen - Emily Lee, Ricky Lin
#SoftDev1 pd06
#K17: Average
#2018-10-09 T

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db" #connect to db

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def compAvg():
    grades = {}  #create new dict of grades
    c.execute("SELECT * FROM peeps, courses WHERE peeps.id == courses.id;") #match students to their appropriate courses
    rows = c.fetchall() #store those values in rows
    for row in rows:  
        if row[2] not in grades: #if the id is unique and not in the dict yet
            counter = 1  #create new counter
            grades[row[2]] = [str(row[0]),row[4]]  #make a new entry with id as key and an array of the name and grade as value
        else:
            counter += 1  #increment counter
            grades[row[2]][1] = (grades[row[2]][1]*(counter-1) + row[4]) / counter  #average the new grade into the existing average
    return(grades)

def peeps_avg(grades):
    c.execute("CREATE TABLE peeps_avg(name STRING, avg INTEGER)")  #create new table with name and average columns
    for idnum,avg in grades.items():  #iterate through grades
        c.execute("INSERT INTO peeps_avg VALUES(" + str(idnum) + ","+ str(avg[1])+")") #insert the student id and respective avg into table

def addcourses(c,g,i):  
    with open("data/courses.csv","a",newline='') as file:  #opens courses csv
        fields=["code","grade","idnum"]  #store the columns as fields
        writer=csv.DictWriter(file,fieldnames=fields) #create writer object to write in csv according to given fields
        writer.writerow({"code":str(c),"grade":str(g),"idnum":str(i)}) #write the given arguments into the csv file

#test functions       
grades=compAvg()
print(grades)
peeps_avg(grades)
#addcourses("x",31,11)
db.commit() #save changes
db.close()  #close database
