
# dictionary data type - MUTABLE
mydict = {
    "firstname": "KIRAN",
    "lastname": "PAUL",
    "age": 30,
    "skills": ["python", "testing"],
    "married": False,
    0: "who put this"
}

print(mydict)
# {'firstname': 'KIRAN', 'lastname': 'PAUL', 'age': 30, 'skills': ['python', 'testing'], 'married': False, 0: 'who put this'}

print(mydict[0])                # who put this
print(mydict["firstname"])      # KIRAN
print(mydict["age"])            # 30
print(mydict["skills"])         # ['python', 'testing']
print(mydict["married"])        # False




# create dictionary at runtime and add data in it

dynamic_dict = {}   # empty dict

dynamic_dict["name"] = "KIRANMOY PAUL"
dynamic_dict["age"] = 30
dynamic_dict["married"] = False
dynamic_dict["sillks"] = ['python', 'devops']

print(dynamic_dict)


