# ==========================================
# PROJECT: LOGIC BOX (PATTERN GENERATOR & NUMBER ANALYZER)
# ==========================================

while True:
    print("\n------------------------------------------")
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("------------------------------------------")
    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip().lower()
    
    if choice == '1' or choice == 'right-angled triangle':
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Error: Row count must be positive.")
            continue
        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()
            
    elif choice == '2' or choice == 'pyramid':
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Error: Row count must be positive.")
            continue
        print("\nPattern:")
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(i):
                print("*", end=" ")
            print()
            
    elif choice == '3' or choice == 'left-angled triangle':
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Error: Row count must be positive.")
            continue
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("  " * (rows - i), end="")
            for j in range(i):
                print("*", end=" ")
            print()
            
    elif choice == '4' or choice == 'analyze a range of numbers':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if end < start:
            print("Error: The end of the range must be greater than or equal to the start.")
            continue
        
        total_sum = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total_sum += num
        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")
        
    elif choice == '5' or choice == 'exit':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice! Please select a valid option from 1 to 5.")