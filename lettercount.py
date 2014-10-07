from sys import argv

script, filename = argv

text = open(filename)
filetext = text.read()
filetext.lower()
text.close()

lowers = 'abcdefghijklmnopqrstuvwxyz'
full_text = []

for i in range(len(lowers)):
    full_text.append(0)

for char in filetext:
    if char in lowers:
        index = lowers.index(char)
        full_text[index] += 1

print full_text






