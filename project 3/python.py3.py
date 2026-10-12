print()
print()
print('Welcome To The Student Data Organizer...!!')
students = []
subjects = set()
id = 101

while True:
    print()
    print('Select An Option...!!')
    print()
    print('-------------------------------------------------')
    print('| Enter 1 For Add Student.                      |')
    print('| Enter 2 For Display All Students.             |')
    print("| Enter 3 For Update Student's Information.     |")
    print('| Enter 4 For Delete Student.                   |')
    print('| Enter 5 For Display Subjects Offered.         |')
    print('| Enter 6 For Exit .                            |')
    print('-------------------------------------------------')
    print()
    print()
    
    choice = int(input('Enter Your Choice :- '))
    print()
    print()
    
    if choice == 1:
        print('Student Id Is :- ', id)
        name = input('Enter Students Name :- ')
        age = int(input('Enter Students Age :- '))
        grade = input('Enter Student Grade :- ')
        dob = input('Enter Student DOB (YYYY-MM-DD) :- ')
        subs_input = input("Enter Subjects (comma-separated) :- ")

        # Split subjects by comma and strip extra whitespaces
        subs_list = [sub.strip() for sub in subs_input.split(',')]
        
        # Add subjects to the global subjects set
        for sub in subs_list:
            subjects.add(sub)

        student = {
            'Id': id,
            'Name': name,
            'Age': age,
            'Grade': grade,
            'Birthdate': dob,
            'Subjects': subs_list
        }
        id += 1
        students.append(student)
        print('Student Added Successfully...!!')
        
    elif choice == 2:
        print()
        print()
        if not students:
            print("No students found.")
        else:
            for stud in students:
                print(f"Student Id :- {stud['Id']}    | Student Name:- {stud['Name']}    | Student Age:-  {stud['Age']}     | Student Grade :-  {stud['Grade']}   | Student Birthdate {stud['Birthdate']}   | Subjects:- {', '.join(stud['Subjects'])}")
        print()
        
    elif choice == 3:
        sid = int(input("Enter Student's id which you want to edit :- "))
        found = False
        for student in students:
            if student['Id'] == sid:
                found = True
                print()
                print('--------------------------------------------------------')
                print('| Enter a For Edit Student Name.                       |')
                print('| Enter b For Edit Student Age.                        |')
                print('| Enter c For Edit Student Grade.                      |')
                print('--------------------------------------------------------')
                print()
                print()
                cho = input('Enter Your Choice For Update Student Details :- ')
                
                if cho == 'a':
                    student['Name'] = input('Enter The New Name Of Student :- ')
                    print('Details Updated Successfully....!!')
                    break
                elif cho == 'b':
                    student['Age'] = int(input('Enter The New Age Of Student :- '))
                    print('Details Updated Successfully....!!')
                    break
                elif cho == 'c':
                    student['Grade'] = input('Enter The New Grade Of Student :- ')
                    print('Details Updated Successfully....!!')
                    break
                else:
                    print('Invalid update choice!')
                break
        if not found:
            print("Student ID not found!")
            
    elif choice == 4:
        sid = int(input("Enter Student's id which you want to remove :- "))
        print()
        print()
        student_to_remove = None
        for student in students:
            if student['Id'] == sid:
                student_to_remove = student
                break
                
        if student_to_remove:
            students.remove(student_to_remove)
            print('Student Removed Successfully...!!')
        else:
            print('Student ID not found!')
            
    elif choice == 5:
        print('----------------------------------------------------------------')
        print('|------------       We Are Offered These Subjects     -------------|')
        if subjects:
            print(f"|   {', '.join(subjects)}   ")
        else:
            print("|   No subjects added yet via students.                        |")
        print('|--------------------------------------------------------------|')
        
    elif choice == 6:
        print()
        print('Thanks For Visiting Visit Again...!!')
        print()
        break
    else:
        print('Please Enter Valid Choice...!!')