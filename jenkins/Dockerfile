FROM jenkins/jenkins:latest

USER root
RUN apt update
RUN apt-get -y install openssh-server
RUN apt-get -y install sshpass 
RUN apt-get -y install python3-pip
RUN apt install python3-pip
RUN python3 -m pip install --user ansible
RUN pip3 install flake8
RUN pip3 install pylint
RUN pip3 install pycode

USER jenkins



