#Task 1
inventory=["bananas","Apples","Corrots","Dates"]
print(inventory)

inventory.append("Eggs")
print(inventory)

inventory.remove("bananas")
print(inventory)

inventory.sort()
print(inventory)


#Task 2
temperatures=[22,24,25,28,30,29,26,24,22]
print(temperatures[0])
print(temperatures[-1])
print(temperatures)

print("Afternoon peak",temperatures[3:6])
print("Last 3Hours",temperatures[-3:])


#Task 3
screen_res=(1920,1080)
print("Current Resolution:1920x1080")
screen_res[0]=1280
print("Tuples cannot be modified!")
