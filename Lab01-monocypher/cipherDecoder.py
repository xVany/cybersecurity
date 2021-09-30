import sys
import math

file = ''
if len(sys.argv) > 2:
    file = sys.argv[1]
    text = open(file).read()
    cipher = sys.argv[2]
    ctext = open(cipher).read()
else:
    print("error provide a filename")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letterfrequency(text): 
    total = 0
    letters = {}
    for letter in alphabet:
        letters[letter] = 0
    for char in text.lower():
        if char in alphabet:
            letters[char] += 1
            total += 1
    for char, count in letters.items():
        letters[char] = count/total
    return letters


def distance(dict1, dict2):
    total = 0
    for char in alphabet:
        total += (dict1[char]-dict2[char])**2
    return math.sqrt(total)


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


englishFreq = letterfrequency(text)
smallestD = distance(letterfrequency(shiftBy(ctext, 0)), englishFreq)
smallestCount = 0
for i in range(1, 26):
    d = distance(letterfrequency(shiftBy(ctext, i)), englishFreq)
    if d < smallestD:
        smallestD = d
        smallestCount = i

print(shiftBy(ctext, smallestCount))
      
