from flask import request
from flask_app import app
from book import Book, topicsearch, itemsearch, updatesearch


###########get book by id########## 
def query_by_item(book_id):
    # Use static method to get book by ID
    return Book.get(book_id)


#########get book by topic############
def query_by_topic(book_topic):
    # Use static method to get books by topic
    return Book.search(book_topic)



############search query using get and parameters##########
@app.route('/query/<method>/<param>', methods=['GET'])
def query(method, param):
###########error if not existed###############
    if method not in queries:
        return {'message': 'Invalid query method', 'supportedQueryMethods': list(queries.keys())}, 404

  

###########error if theere is no value ####################
    if result is None:
        return {'message': 'Not found'}, 404

  


###########update on the dp  using put 
@app.route('/update/<book_id>', methods=['PUT'])
def update(book_id):

    ##############get the data from the req###########
    book_data = request.json

#####if req is empty update none#############
    if book_data is None:
        book_data = {}

    
    book = Book.update(book_id,

                       quantity=book_data.get('quantity'),

                       price=book_data.get('price'))

##########if book is not existed in db return errror message#############3
    if book is None:
        return {'message': 'Not found'}, 404

   
