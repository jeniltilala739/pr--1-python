print()
print()
print('Welcome To The Student Data Organizer...!!')
students = []
subjects =set()
print()
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
    print('| Enter 5 For Display Suibjects Offered.        |')
    print('| Enter 6 For Exit .                            |')
    print('-------------------------------------------------')
    print()
    print()
    choice = int(input('Enter Your Choice :- '))
    print()
    print()
    if choice == 1:
        print('Student Id Is :- ',id)
        name = input('Enter Students Name :- ')
        age = int(input('Enter Students Age :- '))
        grade = input('Enter Student Grade :- ')
        dob = input('Enter Student DOB (YYYY-MM-DD) :- ')
        subs = input("Enter Subjects(comma-separeted) :- ")

        subs.split(',')
        for ab in subjects:
            subjects.add(subs)


        student = {
                    'Id':id,
                    'Name' : name,
                    'Age' : age,
                    'Grade' : grade,
                    'Birthdate': dob,
                    'Subjects' : subs
                }
        id += 1
        students.append(student)
       
    elif choice == 2:
        print()
        print()
        for stud in students:
            print(f'Student Id :- {stud['Id']}    | Student Name:- {stud['Name']}    |Student Age:-  {stud['Age']}     | Student Grade :-  {stud['Grade']}   | Student Birthdate {stud['Birthdate']}   | Subjects:- {stud[subs]}')
        print()
    elif choice == 3:
        sid = int(input("Enter Student's id which you edit :- "))
        for student in students:
            if student['Id'] == sid:
                print()
                print('--------------------------------------------------------')
                print('| Enter a For Edit Student Name.                       |')
                print('| Enter b For Edit Student Age.                        |')
                print('| Enter c For Edit Student Grade.                      |')
                print('--------------------------------------------------------')
                print()
                print()
                cho  = input('Enter Your Choice For Update Student Details :- ')
               
                if cho == 'a':
                    student['Name'] = input('Enter The New Name Of Student :- ')
                    print('Deatils Updated Successfully....!!')
                    break
                elif cho == 'b':
                    student['Age'] = int(input('Enter The New age Of Student :- '))
                    print('Deatils Updated Successfully....!!')
                    break
                elif cho == 'c':
                    student['Grade'] = input('Enter The New Grade Of Student :- ')
                    print('Deatils Updated Successfully....!!')
                    break
    elif choice == 4:
        sid = int(input("Enter Student's id which you remove :- "))
        print()
        print()
        if sid == student['Id']:
            students.remove(student)
        print('Student Removed Successfully...!!')
    elif choice == 5:
        print('----------------------------------------------------------------')
        print('|------------    We Are Offered These Subjects    -------------|')
        print('|      Maths , English , Science , Hindi , Social Science      |')
        print('|--------------------------------------------------------------|')
    elif choice == 6:
        print()
        print('Thanks For Enjoying Visit Again...!!')
        print()
        break
    else:
        print('Please Enter Valid Choice...!!')
