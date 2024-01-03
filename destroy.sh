#!/bin/bash

container_id=$(sudo docker ps | cut -d" " -f 1 | tail -1)

sudo docker stop $container_id
sudo docker rm $container_id
