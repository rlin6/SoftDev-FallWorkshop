#RHCP-Damian Wasilewicz, Ricky line
#SoftDev1 Pd6
#K06--Stl/O:Getting By With a Little Help From Our Friends
#2018-09-13

#imports the necessary libraries for reading csv files and using random
import csv, random

#creates dictionary (empty)
OCCLIST = {}

def occCreate(filename, _dict, begin, end):
#takes in file and returns dictionary

    #opens file and reads it
    try:
        # tries to open the file name
        file = open(filename,'r')
    except:
        # if it cannot open it
        print("File does not exist")
        return 0
    
    red = file.read()
    #split by lines, excluding title and empty line at bottom
    lines = red.split("\n")[1:-1]
    read = csv.reader(lines)
    #iterates through each row        
    for r in read:
        #starts at column after beginning
        col = begin + 1
        val = []
        #iterates through each column, adding each value to a list
        while col <= end:
            try:
                val.append(float(r[col]))
            except:
                val.append(r[col])
            col += 1
        #set beginning as key and the list as value
        _dict[r[begin]] = val
    #to be polite
    file.close()
    return _dict

def randomOcc(_dict):
    #generatoes random float
    randy = random.uniform(0, 99.8)
    #counter keeps track of what percentage we're up to
    count = 0
    #returns key based with weighted probability
    for key, value in _dict.items():
        #compares random number to % we're up to;
        #if current percentage is greater than randy, return key
        if count + value[0] >= randy:
            return key
        #if not, add counter to current percentage
        count += value[0]

print(randomOcc(occCreate("data/occupations.csv", OCCLIST, 0, 2)))
