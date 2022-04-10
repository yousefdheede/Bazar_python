from flask_app import app, catalog_ip
import requests


########### BUY ###########

@app.route('/buy/<book_id>', methods=['PUT'])
def buy(book_id):
    # If the ID is not a number, reject the purchase
    if not book_id.isnumeric():
        return {' ID must be a number'}, 422

    ############ search in catalog for book id ###########
    book_response = requests.get(f'{catalog_ip}/query/item/{book_id}')

    ############ if book not found --> error ! ###########
    if book_response.status_code == 404:
        return {' ID does not fouund'}, 404

    ############ else , if not ok return another error ###########
    elif book_response.status_code != 200:
        return book_response.content, book_response.status_code, book_response.headers.items()

    ############ get book info from response ###########
    book = book_response.json()

    ############ if theres no books in stock ###########
    if book['quantity'] <= 0:
        return {'Book out of stock'}

    buy_response = requests.put(f'{catalog_ip}/update/{book_id}', json={'quantity': book['quantity']-1})

    ############  errors in updating ###########
    if buy_response.status_code != 200:
        return buy_response.text, buy_response.status_code, buy_response.headers.items()

    ############ else success ###########
    return {'Book with ID purchased'}

