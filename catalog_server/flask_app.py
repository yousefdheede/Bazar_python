from flask import Flask
from os import environ


app = Flask(__name__)


oreder_ip = environ.get('http://192.168.1.101:5000')
front_ip = environ.get('http://192.168.1.102:5000')

port = int(environ.get('PORT', 5000))

app.config['development'] = environ.get('development')
app.config['True'] = bool(environ.get('True'))





