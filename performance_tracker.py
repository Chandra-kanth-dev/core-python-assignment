def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input(f"Enter marks for {name} (comma-separated): ").split(',')))
    students[name] = marks

averages = {name: calculate_average(marks) for name, marks in students.items()}
top_student = max(averages, key=averages.get)

print("Average Marks:", averages)
print("Top Performer:", top_student)
