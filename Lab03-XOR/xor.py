import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.


keylen = len(key) - 1
inplen = len(inp) - 1


def xor(inp, key):
    tmp = []
    output = ''
    i = 0
    for val in inp:
        if val != 13: #ignores \n
            tmp.append(val ^ key[i % keylen])
        i += 1

    if mode == "numOut":
        for x in tmp:
            output += hex(x)[2:] + ' '
        return output

    if mode == "human":
        for x in tmp:
            output += chr(x)
        return output

print(xor(inp, key))
