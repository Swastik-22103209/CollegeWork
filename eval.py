def add_student():
    name = input("Enter Student Name: ")
    studentID = input("Enter StudentID: ")
    while(studentID in school.keys()):
        print("Please enter Unique StudentID!!!/n")
        studentID = input("Enter StudentID: ")
    std_class = input("Enter Student Class: ")
    grades = []
    
    for i in range(5):
        grade = int(input("Enter Grade: "))
        grades.append(grade)
       
    std_data = [name, std_class, grades]
    school[studentID] = std_data
    print("Student Succesfully Added to the Database!!!/n")
    
def update_grades():
    studentID = input("Enter Student ID to update Grade: ")

    while(studentID not in school.keys()):
        print("Please enter Correct StudentID!!!/n")
        studentID = input("Enter StudentID to update Grade: ")
        
    data = school[studentID]
    
    grades = data[2]
    
    print("Previous Grades: ", grades)
    
    new_grades = []
    
    for i in range(5):
        grade = int(input("Enter Grade: "))
        new_grades.append(grade)
    
    data[2] = new_grades
    school[studentID] = data
    
    print("Student Grades Succesfully Updated to the Database!!!/n")
    
def calculate_average():
    studentID = input("Enter Student ID to update Grade: ")

    while(studentID not in school.keys()):
        print("Please enter Correct StudentID!!!/n")
        studentID = input("Enter StudentID to update Grade: ")
        
    data = school[studentID]
    
    grades = data[2]
    
    average = 0
    for i in range(5):
        average += grades[i]
        
    average /= 5
    
    return average

def generate_top_students_report():
    #Classes are A, B, C
    A = dict()
    B = dict()
    C = dict()
    
    keys = school.keys()
    
    for i in range(len(school)):
        data = school[keys[i]]
        if(data[1]=='A'):
            A[keys[i]] = data
        elif(data[1]=='B'):
            B[keys[i]] = data
        elif(data[1]=='C'):
            C[keys[i]] = data            
            
    keysA = A.keys()
    stdIDA = ""
    maxMarksA = 0
    for i in range(len(A)):
        data = A[keysA[i]]
        grades = data[2]
        
        marks = 0
        for j in range(5):
            marks += grades[j]
            
        if(maxMarksA<marks):
            maxMarksA = marks
            stdIDA = keysA[i]
            
    print("Student with Top Performance: ")
    print(stdIDA)
    print(A[stdIDA])
        
        
        



main_choice = 0

school = dict()

while(main_choice!=5):
    print("1. Add_Student()")
    print("2. Update_Grades()")
    print("3. Calculate_Average()")
    print("4. Generate_Top_Students_Report()")
    
    main_choice = int(input("Enter your Choice: "))
    print()
    
    if main_choice == 1:
        add_student()
        
    elif main_choice == 2:
        update_grades()
        
    elif main_choice == 3:
        avg_marks = calculate_average()
        print("Average Marks = ", avg_marks)
        
    elif main_choice == 4:
        generate_top_students_report()