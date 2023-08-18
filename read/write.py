#!/usr/bin/python3

file = open('source_file')
a = file.readlines
i = 0
filea = open('flippy.log', 'w')

for line in file:
    print(line, end='')
    filea.write(line)
    


file.close
