# web (application)
from flask import Flask,render_template,jsonify, request, session
import datetime
from flask_socketio import SocketIO, emit
#from . import config

app = Flask(__name__)
app.secret_key = "secret"
socketio = SocketIO(app)

@app.route('/')
def hello(): 
    return render_template('index.html')

@socketio.on('connect', namespace='/mynamespace')
def connect():
    print ("Connected")

@socketio.on('disconnect', namespace='/mynamespace')
def disconnect():
    session.clear()
    print ("Disconnected")

@app.route('/result', methods=['POST'] )
def receiveRes():
    res = request.get_json()
    print(res)
    if(res==None):
        res = str(request.get_data())
        res = res[2:-1].split('&')
        if(res[0].find('confidence')>-1):
            res = {'groupName':res[1][-1:],'confidence':float(res[0][res[0].index('=')+1:])}
        else:
            res = {'groupName':res[0][-1:],'confidence':float(res[1][res[1].index('=')+1:])}
        

    mem = "NA"
    if(res.get('confidence') >= 0.5):
        if(res.get('groupName')=='A'):
            mem = 'A'
        elif(res.get('groupName')=='B'):
            mem = 'B'

    socketio.emit('response',{'data': mem},broadcast=True,namespace='/mynamespace' )
    return mem   
    
@socketio.on_error(namespace='/mynamespace')
def chat_error_handler(e):
    print('An error has occurred: ' + str(e))


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port="5005")
