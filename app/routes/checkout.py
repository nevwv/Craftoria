from flask import render_template, redirect, url_for, flash
from . import checkout_bp  # Импортируем Blueprint из текущего пакета
from app.models import Order
from app.models import db
from app.models import PaymentMethod, Transaction


@checkout_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    payment_methods = PaymentMethod.query.filter_by(is_active=True).all()
    # Создаем заказ
    new_order = Order(...)
    db.session.add(new_order)
    db.session.commit()
    orders = Order.query.all()
    return render_template('checkout.html', orders=orders)
