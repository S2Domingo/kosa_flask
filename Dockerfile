FROM python:3.8.4

USER root
WORKDIR /root

# bse
# RUN apt-get -y update
# RUN apt-get -y install python3-pip

# flask
WORKDIR /app

COPY ./app/ app/
COPY ./config.py config.py
COPY ./requirements.txt requirements.txt

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt



ENV FLASK_APP=app

CMD flask run --host 0.0.0.0 -p 80
