#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo 'Error: Please run as root'
  exit 1
fi

apt-get install -y openssh-server apache2 mysql-server vsftpd git 

git clone https://github.com/anxolerd/dvpwa.git
