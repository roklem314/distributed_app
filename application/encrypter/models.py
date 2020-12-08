from application import db,app

class Ciphertext(db.Model):

    __tablename__ = "ciphertext"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    ciphertext = db.Column(db.String())
    key = db.Column(db.String())

    def __init__(self,ciphertext,key):
        self.ciphertext = ciphertext
        self.key = key

    def __repr__(self):
        return self.id
