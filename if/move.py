#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""


import shutil   
import os      

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/if') 

    xname = input('What is the new name for kerrigan.obj? ') 
    shutil.move('moveme.txt', xname)


main() 

