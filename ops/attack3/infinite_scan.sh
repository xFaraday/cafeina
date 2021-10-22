#!/bin/bash

while true; do
  nmap -T2 -sV -Pn defense --script=./vulners.nse -p10000-25535
  sleep 5;
done
