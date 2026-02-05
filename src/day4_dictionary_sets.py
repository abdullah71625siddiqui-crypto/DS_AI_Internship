#Task 1
contacts = {
    "akash": "555-1234","Bob": "555-5678","raj": "555-9012"}

contacts["handy"] = "555-3456"
contacts["Bob"] = "555-0000"

print("akash:", contacts.get("akash", "Contact not found"))
print("kanye:", contacts.get("kanye", "Contact not found"))

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
    
    
#Task 2

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

print("Is ID05 in unique_users?", "ID05" in unique_users)

print("Original log count:", len(raw_logs))
print("Unique user count:", len(unique_users))

print("Unique Users:", unique_users)

#Task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print("Interests they both share are:",friend_a&friend_b)
print("Unique interests between the two are:",friend_a|friend_b)
print("Unique interests of a are:",friend_a-friend_b)