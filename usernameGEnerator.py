full_name = input("Enter your full name: ") 
 
name_parts = full_name.strip().split() 
 
username = "" 
 
# Build username based on number of parts 
if len(name_parts) == 1: 
    username = name_parts[0].lower() 
elif len(name_parts) == 2: 
    username = name_parts[0][0].lower() + name_parts[1].lower() 
else: 
    username = name_parts[0][0].lower() + name_parts[1][0].lower() + name_parts[
1].lower() 
 
print(f"Generated Username: {username}") 
