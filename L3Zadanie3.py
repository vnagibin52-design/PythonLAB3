import timeit

my_list = []

for i in range(100):
    my_list.append(i)

my_set = set(my_list)

for val in (90, -1):
    t_list = timeit.timeit(lambda: val in my_list, number=100)
    t_set  = timeit.timeit(lambda: val in my_set, number=100)
    print("100", val, t_list, t_set)

my_list.clear
for i in range(10000):
    my_list.append(i)

my_set = set(my_list)

for val in (9000, -1):
    t_list = timeit.timeit(lambda: val in my_list, number=100)
    t_set  = timeit.timeit(lambda: val in my_set, number=100)
    print("10000", val, t_list, t_set)

my_list.clear
for i in range(1000000):
    my_list.append(i)

my_set = set(my_list)

for val in (900000, -1):
    t_list = timeit.timeit(lambda: val in my_list, number=100)
    t_set  = timeit.timeit(lambda: val in my_set, number=100)
    print("1000000", val, t_list, t_set)
