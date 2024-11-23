age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)


# age = int(input("Enter your age:"))
# day = input("Enter day:")

# if age >= 18:
#     if day == "wednesday":
#         print("Ticket Price for you is $10")
#     else:
#         print("Ticket Price for you is $12")
# elif day == "wednesday":
#     print("Ticket price for you is $6")
# else:
#     print("Ticket price for you is $8")