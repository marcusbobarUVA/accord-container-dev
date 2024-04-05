FROM quay.io/accord/rockylinux8-mirror:latest

ADD http://worldtimeapi.org/api/timezone/Etc/UTC.txt /timestamp

RUN chmod 0644 /timestamp
RUN dnf -y update && \
  dnf -y install \
    bzip2 \
    gcc \
    gcc-c++ \
    git \
    jq \
    less \
    make \
    patch \
    openssl-devel \
    libcurl-devel \
    python3.9 \
    python3-pip \
    unzip \
    vim-minimal \
    which \
    xz && \
    unlink /usr/bin/python3 && \  
    ln -sf /usr/bin/python3.9 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.9 /usr/bin/python && \
    unlink /usr/bin/pip3 && \
    ln -sf /usr/bin/pip3.9 /usr/bin/pip3 && \
    unlink /usr/bin/pip-3 && \
    ln -sf /usr/bin/pip-3.9 /usr/bin/pip-3 && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    dnf clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/dnf.* && \
    groupadd --gid 490 user && \
    groupadd --gid 491 project && \
    useradd --home-dir /home/user --uid 490 --gid 490 user && \
    mkdir /home/project && \
    chown root:project /home/project && \
    chmod 775 /home/project
ENV PYTHONPATH=/home/user/.local
ENV LC_ALL=C.utf8
ENV LANG=en_US.UTF-8
# ADD ./centos8-base/sh.local /etc/profile.d/sh.local
RUN echo "export PATH=$PATH:/home/user/.local:/home/user/.local/bin" >> /etc/profile
RUN echo "export PATH=$PATH:/home/user/.local:/home/user/.local/bin" >> /etc/bashrc
