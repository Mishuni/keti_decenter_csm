FROM python:3.6

EXPOSE 5000
ENV APP /www

RUN mkdir $APP
ADD . $APP
WORKDIR $APP

RUN python -m pip install --upgrade pip 
RUN pip3 install Flask uwsgi pytz

# run uWSGI with the ini file
CMD uwsgi uwsgi.ini
