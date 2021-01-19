#https://www.youtube.com/watch?v=bD05uGo_sVI
"""def square_numbers(nums):
    result= []
    for i in nums:
        result.append(i*i)
    return result"""

def square_numbers(nums):
    for i in nums:
        yield (i*i)

#generator don't hold entire result in memory, yield one result at a time

my_nums =  square_numbers([1,2,3,4,5,6,7,8])

print(my_nums) # hasn't computed anything yet

print(next(my_nums))
print('***')
iter = 0
for num in my_nums:
    iter += 1
    if iter >2:
        break
    print(num)

print("***")
print(next(my_nums))


#list comprehension often in python
#my_nums = [ x*x for x in [1,2,3,4,5,6]]

#generator comprehension
my_nums = ( x*x for x in [1,2,3,4,5,6])

#convert generator to list
list(my_nums)