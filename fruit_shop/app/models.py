from app import db

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    variety = db.Column(db.Text)
    type = db.Column(db.Text)
    price_cents = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.variety} {self.type} x {self.quantity}'
    
