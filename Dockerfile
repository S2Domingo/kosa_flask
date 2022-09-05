FROM python:3.8.4

USER root
WORKDIR /root

# bse
# RUN apt-get -y update
# RUN apt-get -y install python3-pip

# flask
WORKDIR /app

COPY static/ static/
COPY templates/ templates/
COPY app.py app.py

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Create DB
RUN python -c "from app import db; db.create_all()"
ENV FLASK_APP=app


CMD flask run --host 0.0.0.0 -p 80
