input_str = input("Enter String:")

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is:", char)
        break # ye continue se different h usme to vo particular iteration ko skip krta tha isme pura loop khtm hojata h
