import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()
inp = open(inpfile,"rb").read()


keylen = len(key)
inplen = len(inp)


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
        with open('output', 'wb') as f:
            for x in tmp:
                f.write(x.to_bytes(1, byteorder="little"))

print(xor(inp, key))
