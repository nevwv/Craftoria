from flask import request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, User
from . import profile_bp  # Импортируем blueprint из текущего пакета


@profile_bp.route('/save_profile', methods=['POST'])
@login_required
def save_profile():
    try:
        user = User.query.get(current_user.id)
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.phone = request.form['phone']

        db.session.commit()
        flash('Данные сохранены!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Ошибка: {str(e)}', 'danger')

    return redirect(url_for('profile.view'))
