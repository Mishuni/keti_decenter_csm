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

# GET method
# @app.route('/calculate')
# def countServer():
#     client = connectDB()
#     val = process_list(client)
#     return val

# @app.route('/result', methods=['POST'])
# def receiveResult():
#     value = request.get_json()
#     print(value.get('confidence'))
#     emit('response',{'data':value.get('confidence'), 'username':value.get('groupName')},broadcast=True)
#     return jsonify(value)

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
    mem = "NA"
    if(res.get('confidence') >= 0.5):
        if(res.get('groupName')=='A'):
            print('A')
            mem = 'A'
        elif(res.get('groupName')=='B'):
            print('B')
            mem = 'B'
    else :
        print("NA")
    socketio.emit('response',{'data': mem},broadcast=True,namespace='/mynamespace' )
    return mem   
    
@socketio.on_error(namespace='/mynamespace')
def chat_error_handler(e):
    print('An error has occurred: ' + str(e))


#if __name__ == '__main__':
    #socketio.run(app, host="0.0.0.0", port="5005")
