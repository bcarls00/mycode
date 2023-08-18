#!/usr/bin/python3

import os
import shutils

def main():
    with open("/home/student/mycode/project/sources/master.conf", "r") as source:
        os.system("touch /home/student/mycode/project/finished/config")
        with open("/home/student/mycode/project/finished/config", "a") as config:
            for line in source:
                if "fast" in source.lower:
                    print(



