no_of_students = int(input("Enter number of students: "))

counter = 0
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

while counter < no_of_students:
    counter += 1
    grade = int(input("Enter student grades: "))
    if grade // 10 == 10:
        a_count += 1
    elif grade // 10 == 9:
        b_count += 1
    elif grade // 10 == 8:
        c_count += 1
    elif grade // 10 == 0:
        d_count += 1
    else:
        f_count += 1

print('===========================')
print("Grade report")
print('===========================')
print(f"Number of students who received each grade: \n"
      f"A: {a_count} \n"
      f"B: {b_count} \n"
      f"C: {c_count} \n"
      f"D: {d_count} \n"
      f"F: {f_count}")


