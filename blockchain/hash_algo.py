import crypto

text1 = "salut tout le monde"
text2 = "salut tout le monde!"

print(crypto.hash256(text1))
print(crypto.hash256(text2))
