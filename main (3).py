class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    student_list.sort(key=lambda student: student.cgpa, reverse=True)

if __name__ == "__main__":
    students = [
        Student("Alice", "101", 3.8),
        Student("Bob", "102", 3.6),
        Student("Charlie", "103", 3.9)
    ]

    print("Before sorting:")
    for student in students:
        print(student)

    sort_students(students)

    print("\nAfter sorting by CGPA (descending):")
    for student in students:
        print(student)