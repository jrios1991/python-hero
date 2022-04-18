# if elif and else statements
# hungry = True
# if hungry:
#     print("Feed me!")
# else:
#     print("I'm not hungry right now.")

# location = "Bank"
# if location == "Auto Shop":
#     print("I need an oil change")
# elif location == "Store":
#     print("I need to get my groceries.")
# else:
#     print(f"I need to go to the {location}")

# for loops
my_iterable = [1,2,3,4,5,6,7,8,9,10]
for item in my_iterable:
    if item % 2 == 0:
        print(item)
    else:
        print(f"Odd Number: {item}")

list_sum = 0
for num in my_iterable:
    list_sum = list_sum + num
    print(list_sum)

for letter in "Hello world":
    print(letter)

tuple = (1,2,3)
for item in tuple:
    print(item)

my_list = [(1,2),(3,4),(5,6)]
for a,b in my_list:
    print(a)

my_dict = {"v1":1, "v2":2, "v3":3}
for key, value in my_dict.items():
    print(key)