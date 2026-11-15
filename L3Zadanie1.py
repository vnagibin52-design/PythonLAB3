my_list = [10, 10, 10, 10, 10, 10]
my_tuple = (20, 20, 20, 20, 20, 20)

print(type(my_list))  
print(id(my_list))    
print(type(my_tuple))  
print(id(my_tuple))    

id_before = id(my_list)
my_list[0] = 99
id_after = id(my_list)

new_tuple = (99, 20, 20, 20, 20, 20)

print(id_before == id_after)  

print(id(my_tuple) == id(new_tuple))