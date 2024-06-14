student_heights = input("input a list of student height").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
student_heights = [180,123,190,173,233,150]
# without len and sum fonction:
totale = 0
for height in student_heights:
    totale += height
    print(totale)
# with len and sum fonction:
totale_student = sum(student_heights)
number_student = len(student_heights)

avreage  = round(totale_student / number_student)
print(avreage)

# what i never think about : 
number_student = 0
for student in student_heights:
    number_student += 1
    print(number_student)