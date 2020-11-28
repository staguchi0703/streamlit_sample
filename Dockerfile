FROM python:3.8.6-slim
COPY ./requestments.txt ./
RUN pip install -U pip
RUN pip install -r requestments.txt