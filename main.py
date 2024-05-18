from flask import Flask,request
import time
app = Flask(__name__)
@app.route('/')
def hello():
    return "<p>hello world</p>"
@app.route('/data',methods = ['POST'])
def data():
    msg = request.form.get('message')
    return msg
if __name__ == "__main__":
    app.run(host='192.168.29.66', port=5000)