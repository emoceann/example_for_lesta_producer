FROM python:3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN chmod +x ./start_app.sh