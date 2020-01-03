student = {
    "name": "Mark",
    "student_id": 12345,
    "feedback": None
}

student["last_name"] = "kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print("i cant add this two together")
    print(error)


print("this code prints")