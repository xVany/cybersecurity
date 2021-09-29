import sys
import letterfrequency
file = ''
if len(sys.argv) > 1:
   file = sys.argv[1]
   text = open(file).read()
else:
   print("error provide a filename")

alpha = "abcdefghijklmnopqrstuvwxyz"


