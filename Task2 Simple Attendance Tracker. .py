def initialize_attendance(student_names):
    attendance = {}
    for student_name in student_names:
        attendance[student_name] = 'Absent'
    return attendance

def mark_attendance(attendance, student_name, status):
    if student_name in attendance:
        attendance[student_name] = status
        print(f'{student_name} is marked as {status}.')
    else:
        print(f'Student {student_name} not found.')

def view_attendance(attendance):
    print("\nAttendance Sheet:")
    for student, status in attendance.items():
        print(f'{student}: {status}')

def main():
    student_names = [
        "arun", "jyothi", "rahul", "joel", "sreeja", "bupender", "aruna",
        "pavan", "ruchi", "ravi", "raghu", "getha", "vishnavi", "sam",
        "priyanka", "raju", "krishna", "sushma", "pranya", "anu", "akash",
        "kriran", "shiva", "afifa", "sofia", "uzma", "sai sri", "ravail",
        "tuba", "vibha"
    ]

    attendance = initialize_attendance(student_names)

    while True:
        print("\nMenu:")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            student_name = input("Enter the student's name: ").lower()
            status = input("Mark as Present or Absent: ").capitalize()
            if status in ['Present', 'Absent'] and student_name in student_names:
                mark_attendance(attendance, student_name, status)
            else:
                print("Invalid input. Please check the student name and status.")
        elif choice == '2':
            view_attendance(attendance)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

