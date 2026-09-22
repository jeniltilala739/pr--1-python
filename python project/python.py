# Project: Fundamental Booster
# Interactive Personal Data Collector

print("=" * 60)
print("     Welcome to the Interactive Personal Data Collector     ")
print("  This program collects personal info, performs casting,   ")
print("      and displays variable types, values, and memory IDs. ")
print("=" * 60)
print()

# Collecting Information Safely
name_input = input("Please enter your name: ")
age_input = input("Please enter your age: ")
height_input = input("Please enter your height in meters (e.g., 1.75): ")
fav_num_input = input("Please enter your favourite number: ")

print("\n--- Data Processing & Type Casting ---")

name = str(name_input)
print(f"-> Name converted to string: {name} | Type: {type(name)}")

# Default values handle karne ke liye agar kuch khali chhod diya ho
try:
    age = int(age_input)
except ValueError:
    age = 0

try:
    height = float(height_input)
except ValueError:
    height = 0.0

try:
    fav_number = int(fav_num_input)
except ValueError:
    fav_number = 0

print(f"-> Age converted to integer: {age} | Type: {type(age)}")
print(f"-> Height converted to float: {height} | Type: {type(height)}")
print(f"-> Favourite number converted to integer: {fav_number} | Type: {type(fav_number)}")

# Arithmetic Calculation (Calculating approximate birth year)
current_year = 2026
approx_birth_year = current_year - age
print(f"\n-> Calculated approx birth year using subtraction operator (-): {approx_birth_year}")

# Display Results, Data Types, and Memory Addresses using type() and id()
print("\n" + "=" * 60)
print("                 SUMMARY OF YOUR INFORMATION               ")
print("=" * 60)

print(f"Name             : {name}")
print(f"  - Data Type    : {type(name)}")
print(f"  - Memory Address: {id(name)}")

print(f"Age              : {age}")
print(f"  - Data Type    : {type(age)}")
print(f"  - Memory Address: {id(age)}")

print(f"Height           : {height}")
print(f"  - Data Type    : {type(height)}")
print(f"  - Memory Address: {id(height)}")

print(f"Favourite Number : {fav_number}")
print(f"  - Data Type    : {type(fav_number)}")
print(f"  - Memory Address: {id(fav_number)}")

print(f"Approx Birth Year: {approx_birth_year}")
print(f"  - Data Type    : {type(approx_birth_year)}")
print(f"  - Memory Address: {id(approx_birth_year)}")

print("-" * 60)
print(f"Your birth year is approximately {approx_birth_year}.")
print("-" * 60)

# Exit Message
print("\nThank you for using the Personal Data Collector!")
print("Keep exploring Python further and happy coding