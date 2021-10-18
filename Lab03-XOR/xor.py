import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)

keylen = key.len()
inplen = inp.len()

def xor(inp, key):
    output = ''
    i = 0
    for val in inp:
        output += val ^ key[i % keylen]
        i += 1
    return hex(int(output))
