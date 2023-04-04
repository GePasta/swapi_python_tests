FROM python:3.11-buster

ENV SERVICE_HOME /usr/local/main
RUN mkdir $SERVICE_HOME
WORKDIR $SERVICE_HOME

ENV PATH $PATH:$SERVICE_HOME

COPY requirements.txt .

RUN apt-get update \
    && python -m pip install --upgrade setuptools pip wheel \
    && pip install -r requirements.txt \
    && rm requirements.txt

