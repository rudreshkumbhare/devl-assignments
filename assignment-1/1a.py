# Name : Rudresh Kumbhare
# PRN : 125B1B213
# Batch : D1

import string
n = int(input("Enter number of lines in the text : "))
print(f"Enter {n} lines : ")
lines = [input() for i in range(n)]

temp = []
for i in lines:
  words = i
  word = words.lower().split()
  temp.extend(word)

mydict = {}
for i in temp:
  mydict[i] = temp.count(i)

print(mydict)

