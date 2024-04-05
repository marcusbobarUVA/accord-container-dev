ARG BASE_TAG
FROM quay.io/accord/theia-jupyter-base:${BASE_TAG}

RUN pip3 install jupyterlab && \
  # smoke test
  jupyter lab --version
# Disable jupyter authentication - provided by authenticating proxy
COPY ./theia-jupyter-base/jupyter_notebook_config.py /usr/local/etc/jupyter/jupyter_notebook_config.py
COPY ./theia-jupyter-base/entrypoint-jupyter.sh /usr/local/bin/

# No changes for jupyter-python
# COPY requirements.txt requirements.txt
# RUN pip3 install --user -r requirements.txt

# Jupyter boilerplate
EXPOSE 8888
WORKDIR /home/user
USER 490
ENV PIP_TARGET=/home/user/.local
ENTRYPOINT [ "entrypoint-jupyter.sh" ]
# /Jupyter boilerplate
