FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install git python3 python3-pip tcpdump sudo libpcap-dev -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install default-jdk
RUN mkdir -p /home/CIC
RUN git clone https://github.com/iPAS/TCPDUMP_and_CICFlowMeter.git
RUN git clone https://github.com/xfaraday/cafeina

EXPOSE 22
EXPOSE 80
EXPOSE 3306

#ADD install.sh /install.sh
#RUN chmod -v +x /install.sh
#RUN bash /install.sh

#ADD run-services.sh /run-services.sh
#RUN chmod -v +x /run-services.sh

#CMD["/run-services.sh"]

WORKDIR /TCPDUMP_and_CICFlowMeter
CMD sh try_me.sh
