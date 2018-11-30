from mongoengine import Document, StringField, IntField

class Bike(Document):
    Model = StringField()
    Dailyfee = IntField()
    Image = StringField()
    Year = IntField()



