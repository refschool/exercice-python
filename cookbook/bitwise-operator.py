#https://stackoverflow.com/questions/2096916/real-world-use-cases-of-bitwise-operators
num = 9
print(format(num, '010b'))
print(format(num, '#010b'))
for i in range(10):
    #print(i, '{0:010b}'.format(i))
    print(i, '{:010b}'.format(i))
# &  and  | or   ~ not  ^  xor >>  << shift right, left
a = 9
b = 8
c=1
print(8^9^9)