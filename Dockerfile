FROM python:3.9-slim

RUN  mkdir /opt/app
RUN  cd  /opt/app

WORKDIR  /opt/app

ADD ./app/hello_world.py .

CMD ["python", "-u", "hello_world.py"]