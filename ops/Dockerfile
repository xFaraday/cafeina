#Dockerfile
FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install git python3 python3-pip -y

#RUN git clone https://github.com/FrankBenavidez/ML-DL-IDS

EXPOSE 22
EXPOSE 80
EXPOSE 3306

ADD install.sh /install.sh
RUN chmod -v +x /install.sh
RUN bash /install.sh

ADD run-services.sh /run-services.sh
RUN chmod -v +x /run-services.sh

CMD["/run-services.sh"]
