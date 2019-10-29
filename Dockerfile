
FROM python:3.7-slim

RUN apt-get update \
  && apt-get install -y \
  git \
  curl \
  wget \
  openssh-client \
  gcc \
  mc

RUN pip3 install --upgrade pip
RUN pip install tensorflow==1.13.1

WORKDIR /root/sources

# COPY ./srcansible/ansiblehosts /etc/ansible

# EXPOSE 8888
CMD ["tail", "-f", "/dev/null"]

