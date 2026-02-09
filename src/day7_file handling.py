# Task1

with open("bbt", "a") as file:
    bbt=input("Enter your name and daily goal:")
    file.write("\n"+bbt)
    
    
with open("bbt", "r") as file:
    content=file.read()
    print(content)
   
    
# Task2

import csv  
with open("student.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       if row[2]=="PASS":
        print(row)    
        
              
            
# Task3
   
file = input("Enter file: ")
try:
    with open(file) as f:
        r = f.read()
        print(r)
except:
    print("Oops! That file doesn't exist yet")

            