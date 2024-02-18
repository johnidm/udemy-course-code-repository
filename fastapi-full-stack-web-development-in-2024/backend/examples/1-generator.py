# from typing import List

# prices: List = [1, 2, 3]

# iter_prices = prices.__iter__()

# print(type(iter_prices))

# print(iter_prices.__next__())
# print(iter_prices.__next__())
# print(iter_prices.__next__())


# class InteratorInfinitive:
    
#     def __init__(self):
#         self.num = 0
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.num += 1
#         return self.num
        
# values = iter(InteratorInfinitive())

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
    
def even_numbers():
    # generate the even_numbers < 20
    even = range( 0, 3, 2 )
    
    i = 0
    
    while i < len(even):
        yield even[i]
        i += 1
    
values = even_numbers()

print(next(values))
print(next(values))
print(next(values))
print(next(values))