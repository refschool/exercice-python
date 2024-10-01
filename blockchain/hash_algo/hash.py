import hashlib

print(format(100,'020b'))

s = "salut"
encoded = s.encode()

print(encoded)
hash = hashlib.sha256(encoded)
""" get the hex version of the hash """
hex = hash.hexdigest()

print("rex : ",bin(hex))

a_string = "abc"

a_byte_array = bytearray(a_string, "utf8")
"""Create bytearray

byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
Convert to binary

    byte_list.append(binary_representation)
Add to list


print(byte_list)

"""