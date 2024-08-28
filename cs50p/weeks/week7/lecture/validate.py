import re

email = input("What is your email: ").strip()

if re.search(r"^\w+@.(\w+\.)?\w+\.ac.in$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")
