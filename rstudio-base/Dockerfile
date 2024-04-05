ARG BASE_TAG
FROM quay.io/accord/rockylinux8-base:${BASE_TAG}
RUN yum install -y libsecret-devel
RUN dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN dnf -y install dnf-plugins-core
RUN dnf config-manager --set-enabled powertools
RUN dnf -y install R
RUN dnf -y install https://s3.amazonaws.com/rstudio-ide-build/server/centos8/x86_64/rstudio-server-rhel-1.4.1082-x86_64.rpm
RUN dnf clean all
RUN rm -rf /var/cache /var/log/dnf* /var/log/dnf.*
RUN chmod 1777 /var/run/rstudio-server
COPY ./rstudio-base/database.conf /etc/rstudio/database.conf
COPY ./rstudio-base/entrypoint-rstudio.sh /usr/local/bin/
