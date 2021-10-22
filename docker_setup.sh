#!/bin/bash

# build the network
docker network create --driver bridge attack-net

# build the images
docker build -t "defense:Dockerfile" ./ops/defense
docker build -t "attack:Dockerfile" ./ops/attack
docker build -t "attack2:Dockerfile" ./ops/attack2
docker build -t "attack3:Dockerfile" ./ops/attack3

# run the containers (in this order!)
docker run -dit --name defense --network attack-net defense:Dockerfile bash
docker run -dit --name attack --network attack-net attack:Dockerfile bash
docker run -dit --name attack2 --network attack-net attack2:Dockerfile bash
docker run -dit --name attack3 --network attack-net attack3:Dockerfile bash

# wait for the fun to begin
sleep 5

# begin attack and record execution
docker exec -d defense ./try_me.sh
docker exec -d attack slowloris defense
./ops/attack2/infinite_attack.sh
./ops/attack3/infinite_scan.sh
