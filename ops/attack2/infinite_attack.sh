#!/bin/bash

while true; do
  sh run_attack.sh ssh_login
  sh run_attack.sh stp_login
  sleep 5;
done
