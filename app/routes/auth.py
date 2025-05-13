from flask import request, redirect, url_for, flash
from flask_login import login_user
from app.models import db, User
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        login_user(user)
        flash('Вход выполнен!', 'success')
        return redirect(url_for('profile.view'))
    else:
        flash('Неверный email или пароль', 'danger')
        return redirect(url_for('auth.login_form'))