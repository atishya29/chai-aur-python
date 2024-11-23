score = 185

if score >= 101:
    print("Please verify your score again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)



# score = int(input("Enter your score:"))

# if score >= 90:
#     print("Your Grade is A")
# elif score >= 80:
#     print("Your Grade is B")
# elif score >= 70:
#     print("Your Grade is C")
# elif score >= 60:
#     print("Your Grade is D")
# else:
#     print("Your Grade is F")