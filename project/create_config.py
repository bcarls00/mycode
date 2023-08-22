#!/usr/bin/python3



def create_c(src, dest):
    
    import os
    import shutil
    import csv
    
    with open(src, "r") as source:

#Create config file to paste to

        os.system("touch /home/student/mycode/project/finished/config")

        with open("/home/student/mycode/project/finished/config", "a") as config:
            print("en\nconf t", file=config)

#create and assign vlans

            for line in source:
                intf = line.split(",")
                if "vlan" in line.lower():
                    print(f"interface vlan {intf[1]}", file=config)
                    print(f"ip address {intf[2]} {intf[3]}", file=config)
                    print("exit", file=config)
  
#assign ports fa

                if "fa" in line.lower():
                    print(f"interface {intf[0]}", file=config)
                    if intf[1].lower() == "on":
                        print("no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[2].lower() == "on":
                        print(f"swithcport mode access\nswitchport access vlan {intf[3]}", file=config)
                    
                    print("exit", file=config)
                
#assign ports gi

                if "gi" in line.lower():
                    print(f"interface {intf[0]}", file=config)
                    if intf[1].lower() == "on":
                        print(f"no shutdown", file=config)
                    else:
                        print("shutdown", file=config)
                    
                    if intf[2].lower == "on":
                        print(f"switchport mode access\nswitchport access vlan {intf[3]}", file=config)
                    
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
     
    destfile = dest + hostname + ".conf"

    shutil.move("/home/student/mycode/project/finished/config", destfile)
    shutil.copy("/home/student/mycode/project/sources/master.conf", "/home/student/mycode/project/bu_confs/master_{hostname}.conf")
