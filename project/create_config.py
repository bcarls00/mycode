#!/usr/bin/python3

import os
import shutil

def main():
    with open("/home/student/mycode/project/sources/master.conf", "r") as source:

        os.system("touch /home/student/mycode/project/finished/config")

        with open("/home/student/mycode/project/finished/config", "a") as config:
            print("en\nconf t", file=config)

#create and assign vlans

            for line in source:
                intf = line.split(" ")
                if "vlan" in line.lower():
                    print(f"interface vlan {intf[1]}", file=config)
                    print(f"ip address {intf[3]} {intf[4]}", file=config)
                    print("exit", file=config)
                
                
  
#assign ports fa

                if "fa" in line.lower():
                    intf = line.split(" ")
                    print(f"interface {intf[0]} {intf[1]}\n", file=config)
                    if intf[3].lower() == "yes":
                        print(f"no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[4] == "yes":
                        print(f"swithcport mode access\nswitchport access vlan {intf[5]}", file=config)
                    
                    print("exit", file=config)
                
#assign ports gi
                if "gi" in line.lower:
                    intf = line.split(" ")
                    print(f"interface {intf[0]} {intf[1]}\n", file=config)
                    if intf[3].lower == "yes":
                        print(f"no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[4] == "yes":
                        print(f"swithcport mode access\nswitchport access vlan {intf[5]}", file=config)
                    
                    print("exit", file=config)


main()



