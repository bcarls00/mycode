#!/usr/bin/python3

count = 0

with open("dracula.txt", "r") as drac:
    for line in drac:
        if "vampire" in line.lower():
            print(line)
            count += 1
            with open("vps.txt", "a") as vps:
                print(line, file=vps)
                
print(f"vampire was mentioned {count} times.")
with open("vps.txt", "a") as vps:
                print(f"vampire was mentioned {count} times.", file=vps)
