ARG VARIANT=3-bookworm
FROM python:${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get purge -y imagemagick imagemagick-6-common 

RUN python3 -m pip install --upgrade \
    setuptools==69.0.3 \
    gitpython==3.1.41