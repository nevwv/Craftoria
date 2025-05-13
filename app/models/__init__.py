
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .user import User
from .order import Order
from .payment import PaymentMethod, Transaction
from .order_item import OrderItem

__all__ = ['db', 'User', 'Order', 'PaymentMethod', 'Transaction']



class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    bio = db.Column(db.Text)
    skills = db.Column(db.String(200))
    location = db.Column(db.String(100))  # Для Яндекс.Карт

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

from .order import Order
from .payment import PaymentMethod, Transaction