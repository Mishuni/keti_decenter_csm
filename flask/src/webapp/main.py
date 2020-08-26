import eventlet
eventlet.monkey_patch()
from flask import Flask,render_template,jsonify,request,session
from flask_socketio import SocketIO
# from .logic import process_list, connectDB
#from . import config
import config
from random import randint,random

import datetime,time, pytz, copy
import json
import logging

# 로그 생성
logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()

utc=pytz.UTC
app = Flask(__name__)
app.config['SECRET_KEY'] = 'seceret'
limit = config.RESULT_CONFIG['limit']
threshold = config.RESULT_CONFIG['threshold']
socketio = SocketIO(app)

@app.route('/')
def hello(): 
    return render_template('index.html')

# collect result of A,B
@app.route('/result', methods=['POST'])
def getResult():
    res = request.get_json()
    if(res==None):
        res = str(request.get_data())
        res = res[2:-1].replace("'",'"')
        res = json.loads(res)
    res["confidence"]=float(res["confidence"])
    if(res["groupName"]=="A"):
        socketio.emit('responseA',data=res,broadcast=True,namespace='/socket.io/mynamespace' )
    elif(res["groupName"]=="B"):
        socketio.emit('responseB',data=res,broadcast=True,namespace='/socket.io/mynamespace' )
    
    
    return res


### socket
@socketio.on('connect', namespace='/socket.io/mynamespace')
def connect():
    logging.info("Connected")

@socketio.on('disconnect', namespace='/socket.io/mynamespace')
def disconnect():
    session.clear()
    logging.info("Disconnected")

# File
@socketio.on('file_update', namespace='/socket.io/mynamespace')
def upate_file(timeList):

    return timeList[0]

if __name__ == '__main__':  
    #app.run(host="0.0.0.0",port=9000, debug=True)
    socketio.run(app, host="0.0.0.0",port=5000, debug=True)
    #socketio.run(app, host="0.0.0.0",port=5000, use_reloader=False, debug=True)
