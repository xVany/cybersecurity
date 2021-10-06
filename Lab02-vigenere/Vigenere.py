import sys

if len(sys.argv) > 3:
    func = sys.argv[1]
    textfile = sys.argv[2]
    tfile = open(textfile).read()
    keyfile = sys.argv[3]
    kfile = open(keyfile).read()
else:
    print("provide a textfile, a keyfile, and a function")

text = ""
key = ''
for line in tfile:
    if line.strip():
        text += line

for line in kfile:
    if line.strip():
        key += line


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftBy(text, num):
    new = ''
    for char in text:
        if alphabet.find(char) != -1:
            new += alphabet[(alphabet.find(char) + num) % 26]
        elif alphabet_upper.find(char) != -1:
            new += alphabet_upper[(alphabet_upper.find(char) + num) % 26]
        else:
            new += char
    return new

def encode(text, key):
    i = 0
    cipher = ''
    for char in text:
        letter = key[i % len(key)]
        shift = alphabet.find(letter.lower())
        cipher += shiftBy(char, shift)
        i += 1
    return cipher.upper()


def decode(text, key):
    i = 0
    eng = ''
    for char in text:
        letter = key[i % len(key)]
        shift = alphabet.find(letter.lower())
        eng += shiftBy(char, 26 - shift)
        i += 1
    return eng.upper()

if func == "encode":
    print(encode(text, key))
elif func == "decode":
    print(decode(text, key))
else:
    print("provide a function")
