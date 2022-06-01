FROM mariadb

RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive
RUN mkdir /run/sshd
RUN apt install -y apt --no-install-recommends python3 openssh-server sudo
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
RUN echo 'root:toor' | chpasswd

EXPOSE 22

EXPOSE 3307

CMD ["bash", "-c", "/etc/init.d/mariadb start; /usr/sbin/sshd -D"]
