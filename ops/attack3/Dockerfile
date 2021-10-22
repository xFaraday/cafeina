#Dockerfile
FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install git python python3 python3-pip cron nmap -y
RUN git clone https://github.com/vulnersCom/nmap-vulners
RUN git clone https://github.com/xfaraday/cafeina
RUN nmap --script-updatedb
#RUN mv /cafeina/ops/attack3/infinite_scan.sh .
#RUN chmod 0744 /cafeina/ops/attack3/infinite_scan.sh

EXPOSE 22
EXPOSE 80
EXPOSE 3306

#ADD install.sh /install.sh
#RUN chmod -v +x /install.sh
#RUN bash /install.sh

#ADD run-services.sh /run-services.sh
#RUN chmod -v +x /run-services.sh

#CMD["/run-services.sh"]
#CMD sh infinite_scan.sh

