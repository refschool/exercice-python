import re
#https://www.youtube.com/watch?v=K8L6KVGG-7o
text = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ



"""

pattern = re.compile(r'.?')

matches = pattern.finditer(text)

for match in matches:
    print(match)