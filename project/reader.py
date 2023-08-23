#!/usr/bin/python3

def readit(source,destination):

    from datetime import datetime

    password = input("Current switch password: ")

    with open(source, "r") as source:
        with open(destination, "a") as destination:
            v = []
            d = []
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), file=destination)
            for line in source:
                word = line.split()
                if "hostname" in line.lower():
                    print("hostname: " + word[1], file=destination)
                elif "Vlan" in line:
                    v.append(word[1].strip("Vlan"))
                elif "fastethernet" in line.lower():
                    currentport = "f" + word[1].strip("FastEthernet")
                elif "gigabit" in line.lower():
                    currentport = "g" + word[1].strip("GigabitEthernet")
                elif "shut" in line.lower():
                    d.append(currentport)

            print(f"Password: {password}",file=destination)
            print(f"VLANs: {v}", file=destination)
            print(f"Disabled Ports: {d}\n\n", file=destination)


readit("sources/readme.conf", "finished/switches.txt")






