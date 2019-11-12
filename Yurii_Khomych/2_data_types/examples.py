
my_max = "Max"
my_new_max = "Max"

# students = ["Max", "Oleg"]
students = ["Max"]
lost_students = ["Yurii"]

if students:
    print("Students is here!")
    # if "Oleg" in students and "Max" in students: print("Oleg is here!"); print("Max is here!"); print("Max is here!")
    # if "Oleg" in students:
    #     oleg = True
    # else:
    #     oleg = False
    # oleg = True if "Oleg" in students else False
    # if "Oleg" not in students:
    #     raise Exception
    # assert "Oleg" in students, "Oleg not in students"
    # all_fine = False
#     if True:
#         print("something happen")
#         raise AssertionError
# else:
#     if lost_students:
#         print(f"{lost_students}")
#
# assert all_fine is True, "All fine is not True"
# print(f"Final program, students not found) {students}")


a = 1
b = '2'
c = 3
try:
    result = a + b
except Exception as error:
    print("Something broken: \n", error)
    result = 0
else:
    result += c
finally:
    print(result)

print(f"Result {result}")