#!/usr/bin/python3

def get_csv(fileloc, x):

    a= {}

    with open(fileloc, "r") as foo:
        if x == "ip":
            for row in csv.DictReader(foo):
                akeypair = {row['host']: row['ip']}
                a.update(akeypair)
        if x == "user":
            for row in csv.DictReader(foo):
                akeypair = {row['host']: row['user']}
                a.update(akeypair)
        if x == "pass":
            for row in csv.DictReader(foo):
                akeypair = {row['host']: row['user']}
                a.update(akeypair)

    return a 

def main():
    ip = get_csv('csvtest.csv', "ip")
    user = get_csv('csvtest.csv', "user")
    password = get_csv('csvtest.csv', "pass")
    print(ip)
    print(user)
    print(password)

