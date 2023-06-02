#3 lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(student_name, lunch_preference=None):
    if lunch_preference is None:
        lunch_preference = "Mystery Meat"

    print("Student Nme:", student_name)
    print("Lunch Preference:", lunch_preference)

#test
lunch_lady("John", "Pizza")