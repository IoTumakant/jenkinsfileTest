FROM ubuntu

LABEL "about"="This file is to create an ubuntu image with python to run a python app"

MAINTAINER umakantkumar@gmail.com

RUN apt-get update

RUN apt-get upgrade -y

RUN apt install python -y

COPY TimeLog_file.py /home




