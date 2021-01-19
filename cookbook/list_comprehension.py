#https://www.youtube.com/watch?v=3dt4OGnU5sM
nums = [1,2,3,4,5,6,7,8,9,10]
list = []

#usual way
for n in nums:
    list.append(n)

list = [n for n in nums]

# using map lambda

#only even number
list = [n for n in nums if n%2 == 0]


print(list)

#dict comprehension
names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']


my_dict = {name: hero for name, hero in zip(names,heros) if name != 'Peter'}
print(my_dict)

#set comprehension
nums = [1,1,2,1,3,1,2,1,1,3,2,1]
my_set = {n for n in nums}

print(my_set)

#generator comprehension
"""def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)"""
nums = [1,2,3,4]
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)