# Task1

with open("bbt", "a") as file:
    bbt=input("Enter your name and daily goal:")
    file.write(bbt)
    
    
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
   
try:
    with open("nigga", "r") as file:
       print(file.read())
except FileNotFoundError:
     print("File not found")

            