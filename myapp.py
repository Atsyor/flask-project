from flask import Flask, render_template
import os
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("moorhouseassociaties.com" 1883, 60)

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/whereami')
def whereami():
         return "kdua"

@app.route('/hello/<name>')
def foo(name):
	return render_template('index.html', to=name)

@app. route('/btn')
def index():
	print("button clicked")
	client .publish("test/all" , "this is my message to you")

@app.route('/linux')
def mylinux():
	return render_template('linux.html')

@app.route('/python')
def python():
	return render_template('python.html') 


# if __name__=='__main__':
#        app.run(host="0.0.0.0")
