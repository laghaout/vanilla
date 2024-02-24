FROM python:3.10-slim

# Declare the working directory.
WORKDIR /home

# Install Linux utilities.
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install emacs-nox
RUN apt -y install less
RUN apt -y install tree
RUN apt -y install git

# Install Python packages.
RUN python3 -m pip install --upgrade pip
RUN pip3 install --user --upgrade pip
RUN pip3 install pre-commit
RUN pip3 install poetry
RUN pip3 install pytest

# Install the local package.
COPY . .

# Set up SSH access
# RUN apt install -y openssh-server
# RUN mkdir /var/run/sshd
# RUN echo 'root:root123' | chpasswd
# RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# EXPOSE 22
# CMD ["/usr/sbin/sshd", "-D"]

# docker build . -t myimage
# docker run -d -v $(pwd):/home -p 2222:22 myimage  # In detached mode
# docker run -it -v $(pwd):/home -p 2222:22 myimage bash  # In interactive mode
# ssh root@localhost -p 2222
