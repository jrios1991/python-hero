# python mathematical operations
# print(f"addition: {2+1}")
# print(f"subtraction: {10-3}")
# print(f"multiplication: {10*3}")
# print(f"divsion: {10/5}")
# print(f"modulo: {10%5}")
# print(f"power: {10**3}")
# print(f"order of operations: {(2+17)*(2+2)}")

# python variables
# a = 5
# print(a)
# print(a+a)
# a = a*a
# print(a)
# print(type(a))
# a = 20.1
# print(type(a))
# my_income = 2000
# tax_rate = 0.1
# my_taxes = my_income * tax_rate
# print(my_taxes)

# python strings
# string_one = "hello"
# string_two = 'world'
# string_three = string_one + " " + string_two
# print(f"{string_one} {string_two}")
# print(f"{string_one} \n{string_two}")
# print(f"{string_one} \t{string_two}")
# print(len(string_one))
# print(string_three)
# # indexing
# print(string_three[0])
# print(string_three[-3])
# # slicing
# print(string_three[6:])
# print(string_three[:4])
# print(string_three[2:9])
# # step size
# print(string_three[::2])
# print(string_three[::-1])

# immutability
# name = "Jorge"
# last_letters = name[1:]
# print(last_letters)
# print("j" + last_letters)
# letter = "y"
# print(letter * 5)
# print(name.upper())
# print(name.split("r"))

# formatting strings
# print("Hi my name is {f} {l}".format(f="jorge", l="rios"))
# # precison {value:width.precision f}
# result = 100/3333
# print("The result was {r:1.7f}".format(r=result))
# name = "Jorge"
# age = 31
# print(f"Hi my name is {name} and I am {age} years old.")

# Lists
# my_list = [1,2,3]
# print(len(my_list))
# print(my_list[1:])
# another_list = [4,5]
# print(my_list + another_list)
# another_list.append(6)
# print(another_list)
# my_list.pop(1)
# print(my_list)
# new_list = ["a", "r", "x", "y"]
# new_list.sort()
# print(new_list)
# num_list = [1,4,7,11]
# num_list.reverse()
# print(num_list)

# Dictionaries
# my_dict = {"key1": "value 1", "key2":"value2"}
# print(my_dict["key1"])
# prices_lookup = {"apple": 3.00, "orange": 2.00}
# print(prices_lookup["orange"])
# print(prices_lookup.keys())
# print(prices_lookup.values())
# print(prices_lookup.items())

# Tuples
# t = (1,2,3)

# Sets
# my_set = set()
# my_set.add(1)
# print(my_set)
# my_set.add(2)
# print(my_set)
# my_list = [1,1,1,1,2,2,2,2,3,3,3,3,3]
# print(set(my_list))

# myfile = open('myfile.txt')
# contents = myfile.read()
# print(contents)
# myfile.close()

# I/O
# mode = 'r' is read only
# mode = 'w' is write only (will overwrite)
# mode = 'a' is append only (will add on to files)
# mode = 'r+' is reading and writing
# mode = 'w+' is writing and reading (overwrites existing files or creates a new file)
# with open('myfile.txt') as my_file:
#     contents = my_file.read()
#     print(contents)
with open('myfile.txt', mode='r') as my_file1:
    contents = my_file1.read()
    print(contents)