from utils.dec_truncate import truncate
#Getting a user input
pe = float(input("Enter Points Earned:"))
tn = int(input("Enter Total Points:"))

#Exception handling
try:
    grade = (pe/tn) * 100
    truncated_grade = truncate(grade)
    print(f"Grade: {truncated_grade}%")
except ZeroDivisionError:
    print("Total points cannot be zero!")

if grade >= 90:
    print("Grade: A")
elif grade >= 75:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
else:
    print("Fail! Re-attempt.")

