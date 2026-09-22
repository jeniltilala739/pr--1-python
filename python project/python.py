print("-" * 50)
print("Welcome to the Interactive Personal Data Collector!")
print("-" * 50)


name = input("Please enter your name: ")
age_str = input("Please enter your age: ")
height_str = input("Please enter your height in meters (e.g., 1.68): ")
fav_num_str = input("Please enter your favourite number: ")


age = int(age_str)
height = float(height_str)
fav_number = int(fav_num_str)


current_year = 2026
approx_birth_year = current_year - age


print("-" * 50)
print("Thank you! Here is the information we collected")
print("-" * 50)

print(f"Name: {name} (Type: {type(name)}, Memory: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory: {id(fav_number)})")

print("-" * 50)
print(f"Your birth year is approximately {approx_birth_year}.")
print("-" * 50)


print("\nThank you for using the Personal Data Collector!")