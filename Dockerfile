FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /test

COPY ./requirements.txt /test/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /test/requirements.txt
ENV PIP_ROOT_USER_ACTION=ignore
COPY . /test/

EXPOSE 8000

