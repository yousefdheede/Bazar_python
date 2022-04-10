from flask_app import app, port
import routes
import errorhandlers

###################### RUN INSTANS #######################
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
