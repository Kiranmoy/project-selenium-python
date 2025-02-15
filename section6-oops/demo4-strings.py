
firstname = "Kiranmoy"
lastname = "Paul"
age = 30

print(firstname[0])     # K
print(firstname[0:5])   # Kiran

print(firstname + " " + lastname)   # Kiranmoy Paul

print("moy" in firstname)           # True

print("{} {} age = {}".format(firstname, lastname, age))    # Kiranmoy Paul age = 30

print("Kiran.moy.paul".split("."))  # ['Kiran', 'moy', 'paul']

print("   KIRAN    ".strip())       # KIRAN