"""
Solutions for Homework Set 1

Note:   There are many different solutions that are possible with these questions.
        If your not sure if you solved the questions correctly, try running this solution
        and your solution to see if the output is the same!
"""


# Question 1
# =========================================================
def calculate_sum(numbers, total=0):
    for number in numbers:
        total = total + number
    return total


def get_numbers(numbers=[]):
    for i in range(5):
        a = input('enter a number: ')
        numbers.append(int(a))
    return numbers


def question_1():
    numbers = get_numbers()
    print(calculate_sum(numbers))
    # or in a fancier way
    print(sum(numbers))


question_1()
# =========================================================


# Question 2
# =========================================================
def get_names(names=[]):
    for i in range(3):
        new_name = input('enter a name: ')
        names.append(new_name)
    return names


def is_name_too_long(name):
    if len(name) > 5:
        print('this name is too long!')
    else:
        print('this name is just right!')


def question_2():
    names = get_names()
    for name in names:
        is_name_too_long(name)


question_2()







