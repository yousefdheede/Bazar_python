from flask_app import app, port
import routes
import errorhandlers

#the port = 5000 , will import from flask_app.py

##################################### Run the instance ###########################

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
