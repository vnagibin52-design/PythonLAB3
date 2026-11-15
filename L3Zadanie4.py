import sys

fruits = {
    1: "Яблоко",
    2: "Банан",
    3: "Груша",
    4: "Гранат",
    5: "Ананас",
}

print(fruits[3])

n = 50
ids = list(range(n))
texts = [f"значение_{i}" for i in range(n)]

my_list  = list(texts)
my_tuple = tuple(texts)
my_set   = set(texts)
my_dict  = dict(zip(ids, texts))

print(my_dict)

for name, obj in [("список", my_list), ("кортеж", my_tuple),
                  ("множество", my_set), ("словарь", my_dict)]:
    print(name, sys.getsizeof(obj))