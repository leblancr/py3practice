def my_map(my_func, my_iterable):
    result = []
    
    for item in my_iterable:
        new_item = my_func(item)
        result.append(new_item)
    
    return result

nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)
squared = my_map(lambda x: x**2, nums)
subtract_one = my_map(lambda x: x-1, nums)

print(cubed)
print(squared)
print(subtract_one)
print((lambda x, y: x + y)(4, 5))
