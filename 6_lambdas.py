# lambda expression

def multiply(a, b):
    return a * b


print(multiply(10, 10))

# print((lambda x, y: x * y)(10, 10))
#
# # Higher Order Function - get other functions as a parameter or returns a function as an output
# my_list = [i for i in range(10)]
# even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
# square_numbers = list(map(lambda x: x ** 2, my_list))
# # square_numbers = [e ** 2 for e in my_list]
# #
# print(even_numbers)
# print(square_numbers)


# ip_addresses = {'192.168.0.1': 20, '127.0.0.2': 30, '127.0.0.1': 4, '90.173.200.1': 7}
#
# print(sorted(ip_addresses.items()))
# print(sorted(ip_addresses.items(), key=lambda x: x[1]))
