green = 32
black = 30
red = 31


print("\033[1;31;31m Bright Green  \n")

def hilite(string, status, bold):
    attr = []
    if status:
        # green
        attr.append('32')
    else:
        # red
        attr.append('31')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

print(hilite('red',1,1))