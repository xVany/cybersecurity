import sys
import letterfrequency
import math

file = ''
if len(sys.argv) > 2:
   file = sys.argv[1]
   text = open(file).read()
   cipher = sys.argv[2]
   ctext open(cipher).read()
else:
   print("error provide a filename")

alpha = "abcdefghijklmnopqrstuvwxyz"

englishFreq = letterfrequency(file).letters

def highestFreqletter(text):
   highestFreq = 0
   tempLetter = ''
   for letter, freq in letterfrequency(text).items():
      if freq > highestFreq:
         tempLetter = letter
   return tempLetter

x = alpha.find(highestFreqLetter(ctext)) #4
y = alpha.find(highestFreqLetter(file)) #5

def shiftString(

shift = x - y

if shift < 0:
