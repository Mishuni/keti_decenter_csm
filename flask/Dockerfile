FROM python:3.6

EXPOSE 5000
ENV APP /www

RUN mkdir $APP
ADD . $APP
WORKDIR $APP

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# run uWSGI with the ini file
CMD python3 /www/src/webapp/main.py
