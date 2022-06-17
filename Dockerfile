# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /IPv2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install pandas
RUN pip3 install flask
RUN pip3 install socket
RUN pip3 install import csv
RUN pip3 install multiprocessing


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]