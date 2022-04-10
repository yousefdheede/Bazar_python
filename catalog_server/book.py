from database import db, marshmallow, database_init



class Book(db.Model):



    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False,)
    topic = db.Column(db.String(200), nullable=False,)
    quantity = db.Column(db.Integer, nullable=False, default=0,)
    price = db.Column(db.Float, nullable=False)

    ######################### Constructor#########################
    def __init__(self, title, topic, quantity, price):
        self.title = title
        self.quantity = quantity
        self.topic = topic
        self.price = price

    ########################## Static method to search for books based on the topic#########################
    @classmethod
    def search(cls, topic):
        ########################## Returns books that contain the query string, ignoring case#########################
        return Book.query.filter(Book.topic.ilike(f'%{topic}%'))

    ########################## getting book by id #########################
    @classmethod
    def get(cls, id):
        return Book.query.get(id)




########################## add books #########################

    Book('How to get a good grade in DOS in 40 minutes a day', 'distributed systems', 15, 30.00),
    Book('RPCs for Noobs', 'distributed systems', 13, 35.00),
    Book('Xen and the Art of Surviving Undergraduate School', 'undergraduate school', 15, 20.00),
    Book('Cooking for the Impatient Undergrad', 'undergraduate school', 27, 18.00)
    


##########################  Marshmallow  search using topic  #########################
class Topicsearch(marshmallow.Schema):
    class Meta:
        fields = ('id', 'title', 'topic')




##########################  Marshmallow   search by title  #########################
class Itemsearch(marshmallow.Schema):
    class Meta:
        fields = ('title', 'quantity', 'price')




##########################  Marshmallow updating on the data base  #########################
class Updatesearch(marshmallow.Schema):
    class Meta:
        fields = ('title', 'quantity', 'topic', 'price')






