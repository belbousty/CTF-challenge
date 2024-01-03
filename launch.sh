#!/bin/bash

http_port=2080
ssh_port=2022
ftp_port=2021
script_port=2023

sudo docker build -t ctf .
sudo docker run -d -p $http_port:80 -p $ssh_port:22 -p $ftp_port:21 -p $script_port:19 --name CTF ctf
