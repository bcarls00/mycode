#!/usr/bin/python3

import os
import shutil

def main():
    enpass = input("current switch enable password: ")

    with open("/home/student/mycode/project/sources/master.conf", "r") as source:

#Create config file to paste to

        os.system("touch /home/student/mycode/project/finished/config")

        with open("/home/student/mycode/project/finished/config", "a") as config:
            if enpass is True:
                print(f"en\n{enpass}\n\nconf t", file=config)
            else:
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
                    print(f"interface {intf[0]}", file=config)
                    if intf[2].lower() == "on":
                        print("no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[4].lower() == "yes":
                        print(f"swithcport mode access\nswitchport access vlan {intf[5]}", file=config)
                    
                    print("exit", file=config)
                
#assign ports gi

                if "gi" in line.lower():
                    print(f"interface {intf[0]}", file=config)
                    if intf[2].lower() == "on":
                        print(f"no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[4].lower == "yes":
                        print(f"switchport mode access\nswitchport access vlan {intf[5]}", file=config)
                    
                    print("exit", file=config)

#insert hostname                

                if "hostname" in line.lower():
                    hostname = intf[1]
                    print(f"hostname {hostname}", file=config)

#insert enable password

                if "enable" in line.lower():
                    enpass = intf[1]
                    print(f"enable secret {enpass}", file=config)

                if "username" in line.lower():
                    username=intf[1].rstrip("\n")

                if "password" in line.lower():
                    password = intf[1].rstrip("\n")
                    print(f"username {username} password {password}", file=config)


#write hostname, username and password to switch list text file

            with open("/home/student/mycode/project/switch_list.txt", "a") as switches:
                print(f"Hostname: {hostname}\nPassword: {password}\nEnable Password: {enpass}\n\n", file=switches)  

#final exit and writing to startup file

            print("exit", file=config)
            print("copy run start\n\n", file=config)

#copy finished config to hostname.conf file and move the masterfile to the bu_confs directory with new name

#    shutil.move("mv /home/student/mycode/project/finished/config", "/home/student/mycode/project/finished/{hostname}.conf")
#    shutil.copy("cp /home/student/mycode/project/sources/master.conf", "/home/student/mycode/project/bu_confs/master_{hostname}.conf")

main()


