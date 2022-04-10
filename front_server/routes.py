from flask_app import app, catalog_ip, order_ip
import requests


######search usig book topic#######
@app.route('/search/<book_topic>', methods=['GET'])
def search(book_topic):
#######serch book in catalog###############
    response = requests.get(f'{catalog_ip}/query/topic/{book_topic}')

########return catalog response###############
    return response.text, response.status_code, response.headers.items()


#######serch using book id ###############
@app.route('/lookup/<book_id>', methods=['GET'])
def lookup(book_id):
########chech book id if its number###############
    if not book_id.isnumeric():
        return {'message': 'Book ID must be a number'}, 422

#######list the book by its id from the catalog ###############
    response = requests.get(f'{catalog_ip}/query/item/{book_id}')

    ################ if nit found return message ###############
    if response.status_code == 404:
        return {'Book ID does not exist'}, 404

    ################ return acatalog ###############
    return response.text, response.status_code, response.headers.items()


################ BUY prosses ###############
@app.route('/buy/<book_id>', methods=['PUT'])
def buy(book_id):
    ################ if if not found ###############
    if not book_id.isnumeric():
        return {'ID must be a number'}, 422

    ################ Forward order server req ###############
    response = requests.put(f'{order_ip}/buy/{book_id}')

    ################ response from the order ###############
    return response.text, response.status_code, response.headers.items()
