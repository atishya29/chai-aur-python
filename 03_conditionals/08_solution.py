password = input("Enter Password:")
password_len = len(password)

if password_len < 6:
    strength = "Weak"
elif password_len <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password strength is:", strength)