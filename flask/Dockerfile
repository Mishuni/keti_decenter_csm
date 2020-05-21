FROM python:3.6

MAINTAINER Miseon YU <mmms543.keti@gmail.com>
EXPOSE 9000
ENV APP /www

RUN mkdir $APP
ADD . $APP
WORKDIR $APP

RUN python -m pip install --upgrade pip 
RUN pip3 install Flask flask_socketio eventlet gunicorn

RUN apt-get update && apt-get install vim -y
# run uWSGI with the ini file
WORKDIR $APP/src/webapp
CMD gunicorn main:app --worker-class eventlet -w 1 --bind 0.0.0.0:9000 --reload
