ARG BASE_TAG
FROM quay.io/accord/rstudio-base:${BASE_TAG}

# No changes for rstudio-r

# RStudio boilerplate
EXPOSE 8787
ENV USER=user
WORKDIR /home/user
USER 490
ENV PIP_TARGET=/home/user/.local
ENTRYPOINT [ "entrypoint-rstudio.sh" ]
# /RStudio boilerplate
