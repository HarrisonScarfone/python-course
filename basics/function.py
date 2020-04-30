# def first_function(name):
#     print('Saying hello to ' + name + ' using a function!')
#
#
# first_function('harry')
#
#
# def multiply_by_2(number):
#     return number * 2
#
#
# for i in range(10):
#     print(multiply_by_2(i))


def get_some_stuff(stuff=[]):
    for i in range(5):
        thing = input('enter something for the list: ')
        stuff.append(thing)
    print_a_list(stuff)
    return stuff


def print_a_list(list):
    for item in list:
        print(item)

# print_a_list(get_some_stuff())
# get_some_stuff()



