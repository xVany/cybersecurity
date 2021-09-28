import sys
file = ''
if len(sys.argv) > 1:
   file = sys.argv[1]
   text = open(file).read()
else:
   print("error provide a filename")

alpha = "abcdefghijklmnopqrstuvwxyz"
total = 0
letters = {}
for letter in alpha:
    letters[letter] = 0

for char in text.lower():
    if char in alpha:
        letters[char] += 1
        total += 1
for char, count in letters.items():
    print(char, ":", count/total)
