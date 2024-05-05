from utils.print_with_time import print_with_time

VARIABLE_1 = {"a": 1, "b": 2, "c": 3}
VARIABLE_2 = 123
VARIABLE_3 = 3.14
VARIABLE_4 = "string"
VARIABLE_5 = True
VARIABLE_6 = False
VARIABLE_7 = {1, 2, 3}
VARIABLE_8 = [1, 2, 3]
VARIABLE_9 = (1, 2, 3)
VARIABLE_11 = range(10)
VARIABLE_12 = print

print_with_time("Hello.")
print_with_time(
    "You can print variables like",
    VARIABLE_1,
    VARIABLE_2,
    VARIABLE_3,
    VARIABLE_4,
    VARIABLE_5,
    VARIABLE_6,
    VARIABLE_7,
    VARIABLE_8,
    VARIABLE_9,
    VARIABLE_11,
    "and",
    VARIABLE_12,
)
