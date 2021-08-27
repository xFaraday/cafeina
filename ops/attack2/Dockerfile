#Dockerfile
FROM ubuntu:latest

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install git python3 python3-pip cron -y
RUN git clone https://github.com/lanjelot/patator
RUN git clone https://github.com/danielmiessler/SecLists
RUN git clone https://github.com/xfaraday/cafeina
RUN pip install paramiko
RUN mv /SecLists/Usernames/cirt-default-usernames.txt /SecLists/Passwords/2020-200_most_used_passwords.txt /patator
RUN mv /cafeina/ops/attack2/run_attack.sh /root/
RUN chmod 0744 /run_attack.sh
RUN mv /cafeina/ops/attack2/attack-cron /etc/cron.d/
RUN chmod 0644 /etc/cron.d/attack-cron
RUN crontab /etc/cron.d/attack-cron

EXPOSE 22
EXPOSE 80
EXPOSE 3306

#ADD install.sh /install.sh
#RUN chmod -v +x /install.sh
#RUN bash /install.sh

#ADD run-services.sh /run-services.sh
#RUN chmod -v +x /run-services.sh

#CMD["/run-services.sh"]
