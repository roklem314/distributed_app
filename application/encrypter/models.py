from application import db,app
from application.models import Base

class Ciphertext(Base):

    __tablename__ = "ciphertext"

    ciphertext = db.Column(db.String(500),nullable=False)

    def __init__(self,ciphertext):
        self.ciphertext = ciphertext

    def get_id(self):
        return self.id
