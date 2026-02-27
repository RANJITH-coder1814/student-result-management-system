import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_result_db"
)

cursor = conn.cursor()

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "F"

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    s1 = int(input("Enter Subject1 Marks: "))
    s2 = int(input("Enter Subject2 Marks: "))
    s3 = int(input("Enter Subject3 Marks: "))

    total = s1 + s2 + s3
    percentage = total / 3
    grade = calculate_grade(percentage)

    sql = """INSERT INTO students
             (name, roll_number, subject1, subject2, subject3, total, percentage, grade)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (name, roll, s1, s2, s3, total, percentage, grade)
    cursor.execute(sql, values)
    conn.commit()

    print("Student Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    cursor.execute("DELETE FROM students WHERE roll_number = %s", (roll,))
    conn.commit()
    print("Student Deleted Successfully!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid Choice!")

conn.close()
