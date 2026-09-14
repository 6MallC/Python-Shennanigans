#note unlike lists these require constructors
dictionary= {}
student= {"Fname" : "Connor", "Lname" : "Mall", "age" : "20","mentalstate" : "Crumbling", "year" : "freshman"}
print(student['mentalstate'])
#this is the exercise just its not a book title
student['year']= "sophmore"
print(student['year']) 
set= ()
#again the spirit of the exerise
set= {1,2,3,4,'one','two','three'}
set.add(4)
# no error or change... neat
print(set)