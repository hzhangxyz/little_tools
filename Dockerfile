FROM ubuntu:14.04

MAINTAINER  Trumpet <zh19970205@126.com>

RUN apt-get update && apt-get install -y python python-flask gcc git
RUN git clone https://github.com/zh19970205/little_tools.git /app

CMD "python" "/app/run.py"

EXPOSE 80
