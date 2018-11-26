from mongoengine import Document, StringField, IntField, BooleanField

class Resource(Document):
    name = StringField()
    city = StringField()
    yob = IntField()
    height = IntField()
    weight = IntField()
    available = BooleanField(default= False)
