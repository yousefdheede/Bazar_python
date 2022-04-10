
from flask_app import app, port
import errorhandles
import routes
from database import create_database
create_database()

############################################################
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
