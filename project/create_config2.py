#!/usr/bin/python3

import os
import shutils

def main():
    with open("/home/student/mycode/project/sources/master.conf", "r") as source:
        os.system("touch /home/student/mycode/project/finished/config")
        with open("/home/student/mycode/project/finished/config", "a") as config:
            print("conf t")
            for line in source:
                if "fa" in source.lower:
                    intf = line.right(-15) 
                    print(f"interface {intf}\n")
                    if 