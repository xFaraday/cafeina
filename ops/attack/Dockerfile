#Dockerfile
FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install python python3 python3-pip -y
RUN pip3 install slowloris

EXPOSE 22
EXPOSE 80
EXPOSE 3306

CMD slowloris defense
