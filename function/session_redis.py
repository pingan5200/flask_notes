# pip install redis  
# pip install flask-session  
import redis  
from flask import Flask, request, session
from flask_session import Session


app = Flask(__name__)


app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='47.107.61.133',
                                          port=6379,
                                          password='123456')
Session(app)


@app.route('/login')
def login():
    session['user'] = 'alex'
    return 'fsdffas'


@app.route('/home')
def index():
    print(session.get('user'))
    return '...'

if __name__ == '__main__':
    app.run()


# [root@server src]# ./redis-cli -a 123456
# 127.0.0.1:6379> keys *
# 1) "session:c3a1df3d-f725-4724-bd21-02ec6c5224d5"
