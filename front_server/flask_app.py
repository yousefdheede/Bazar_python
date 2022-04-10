from flask import Flask
from os import environ

################################### Flask application instance##################################
app = Flask(__name__)

###### import the catalog and order ips #############


catalog_ip= environ.get('192.168.1.20:5000')
order_ip= environ.get('192.168.1.197:5000')


#############get the flask configuration from the enviro var ##############


############getiing the ports #'s #################################
port = int(environ.get('PORT', 5000))



app.config['development'] = environ.get('development')
app.config['True'] = bool(environ.get('True'))

 ########

