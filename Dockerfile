FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt update && apt upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt install -y sudo openssh-server apache2 vsftpd curl git unzip

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:ondrej/php && apt update
RUN apt install -y python3
RUN apt install -y python2.7
RUN apt install php7.2 libapache2-mod-php7.2 php7.2-common php7.2-mbstring php7.2-xmlrpc php7.2-soap php7.2-gd php7.2-xml php7.2-cli php7.2-curl php7.2-zip -y

# These should be eliminated after 
RUN apt install nmap netcat systemctl nano -y


# Set up users and their passwords
RUN echo 'root:root' | chpasswd \
    && useradd -ms /bin/bash agent007 \
    && echo 'agent007:agent007' | chpasswd \
    && echo 'www-data:www-data' | chpasswd

RUN service apache2 restart

RUN cd /tmp && wget https://github.com/Jemt/SitemagicCMS/archive/master.zip
RUN unzip /tmp/master.zip
RUN sudo mv SitemagicCMS-master /var/www/html/y0urF1v0r1t3CMS

RUN sudo chown -R www-data:www-data /var/www/html/y0urF1v0r1t3CMS/
RUN sudo chmod -R 755 /var/www/html/y0urF1v0r1t3CMS/
COPY resources/sitemagic.conf /etc/apache2/sites-available/sitemagic.conf

# TCP server : grants access to the file directory

COPY resources/cyber.txt /root/resources/cyber.txt
COPY script.py /root/server.py

# Python script to elevate priveleges from www-data to agent007

RUN mkdir /var/mission/
COPY resources/wdata-a007.py /var/mission/missions.py
COPY resources/missions.txt /var/mission/missions.txt
RUN chown agent007:agent007 /var/mission/missions.py
RUN chmod +x /var/mission/missions.py


# add the capability of running the script of the first privesc as agent007
# add the capability of running the script of the second privesc as root
COPY resources/sudoers /etc/sudoers


# Python vulnerable prompt
COPY resources/builtins.py  /home/agent007/weapons.py
RUN mkdir /home/agent007/resources
COPY resources/weapons.txt /home/agent007/weapons.txt
RUN chown root:root /home/agent007/weapons.txt /home/agent007/weapons.py
RUN chmod -R 711 /home/agent007/weapons.txt /home/agent007/weapons.py

# Vulnerable CMS
RUN a2ensite sitemagic.conf
RUN a2enmod rewrite
RUN service apache2 restart


RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY resources/tcpserver /etc/systemd/system/tcpserver
COPY resources/vsftpd.conf /etc/vsftpd.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]