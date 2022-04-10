from flask import Flask
from os import environ

######################################### instance  ######################################


app = Flask(__name__)



###################### importing the adresses from other environment.#######################

catalog_ip = environ.get('http://192.168.1.20:5000')

front_ip = environ.get('http://192.168.1.85:500')


###################################application port##############################################
port = int(environ.get('PORT', 5000))



######################### environment settings from the environment variables####################

app.config['development'] = environ.get('development')

app.config['True'] = bool(environ.get('True'))



