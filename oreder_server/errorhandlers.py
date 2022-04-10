from flask_app import app


@app.errorhandler(404)
def not_found(e):
    return {'message': 'the URL you applied not found on the server, error 404.'}, 404
###################################################################################################

@app.errorhandler(500)
def internal_server_error(e):
    return {'message': 'the URL you applied not found on the server, error 500.'}, 500
###################################################################################################

@app.errorhandler(405)
def method_not_allowed(e):
    return {'message': 'The method is not allowed 405 .'}, 405
###################################################################################################
