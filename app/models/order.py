from . import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='pending')
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Данные доставки
    shipping_address = db.Column(db.String(200))
    shipping_city = db.Column(db.String(50))
    shipping_postal_code = db.Column(db.String(10))
    notes = db.Column(db.Text)

    items = db.relationship('OrderItem', backref='order', lazy=True)
    transactions = db.relationship('Transaction', backref='order', lazy=True)