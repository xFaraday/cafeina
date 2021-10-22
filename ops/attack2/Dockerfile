#Dockerfile
FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install git python python3 python3-pip cron -y
RUN git clone https://github.com/lanjelot/patator
RUN git clone https://github.com/danielmiessler/SecLists
RUN git clone https://github.com/xfaraday/cafeina
RUN pip3 install paramiko
RUN mv /SecLists/Usernames/cirt-default-usernames.txt /SecLists/Passwords/2020-200_most_used_passwords.txt /patator
RUN mv /cafeina/ops/attack2/run_attack.sh /patator
RUN mv /cafeina/ops/attack2/infinite_attack.sh /patator
RUN chmod 0744 /patator/run_attack.sh
RUN chmod 0744 /patator/infinite_attack.sh
#RUN mv /cafeina/ops/attack2/attack-cron /etc/cron.d/
#RUN chmod 0644 /etc/cron.d/attack-cron
#RUN crontab /etc/cron.d/attack-cron

EXPOSE 22
EXPOSE 80
EXPOSE 3306

WORKDIR /patator
CMD sh infinite_attack.sh
