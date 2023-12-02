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
