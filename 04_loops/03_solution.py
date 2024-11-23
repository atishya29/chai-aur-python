number = int(input("Enter a nummber:"))

for i in range(1, 11):
    if i == 5:
        continue  # ye continue jo bhi humne detection or conditional check kia h sirf us iteration ko bhar nikal dega
    print(number, "X", i, "=", number*i)


# 3 X 1 = 3
# 3 X 2 = 6