import hashlib
import binascii

s = "salut"
encoded = s.encode()

print(encoded)
hash = hashlib.sha256(encoded)
""" get the hex version of the hash """
hex = hash.hexdigest()

print("hex : ",hex)



intervalle = [i for i in range(0,4096)]
print(intervalle)
for i in intervalle:
    nonce = str(i)
    binary = bin(int(nonce + hex,16))
    print(format(binary))

print(format(10,'010b'))