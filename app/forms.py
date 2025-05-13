from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SelectField, RadioField, validators
from wtforms.validators import DataRequired, Length, Email, Regexp
import re


class ProfileForm(FlaskForm):
    first_name = StringField('Имя', validators=[
        DataRequired(message="Поле обязательно для заполнения"),
        Length(min=2, max=50, message="Имя должно быть от 2 до 50 символов")
    ])

    last_name = StringField('Фамилия', validators=[
        DataRequired(message="Поле обязательно для заполнения"),
        Length(min=2, max=50, message="Фамилия должна быть от 2 до 50 символов")
    ])

    email = EmailField('Email', validators=[
        DataRequired(message="Поле обязательно для заполнения"),
        Email(message="Введите корректный email")
    ])

    phone = TelField('Телефон', validators=[
        DataRequired(message="Поле обязательно для заполнения"),
        Regexp(r'^\+?[1-9]\d{10,14}$', message="Введите телефон в формате +71234567890")
    ])


class CheckoutForm(FlaskForm):
    first_name = StringField('Имя', [
        validators.DataRequired(message="Введите имя"),
        validators.Length(min=2, max=50, message="Имя должно быть от 2 до 50 символов")
    ])

    last_name = StringField('Фамилия', [
        validators.DataRequired(message="Введите фамилию")
    ])

    phone = StringField('Телефон', [
        validators.DataRequired(message="Введите телефон"),
        validators.Regexp(r'^\+?[78]\d{10}$', message="Формат: +7XXXXXXXXXX")
    ])

    email = StringField('Email', [
        validators.DataRequired(message="Введите email"),
        validators.Email(message="Некорректный email")
    ])

    address = StringField('Адрес', [
        validators.DataRequired(message="Введите адрес")
    ])

    apartment = StringField('Квартира')

    city = StringField('Город', [
        validators.DataRequired(message="Введите город")
    ])

    postal_code = StringField('Почтовый индекс', [
        validators.Regexp(r'^\d{6}$', message="Индекс должен содержать 6 цифр")
    ])

    notes = TextAreaField('Комментарий к заказу')

    payment_method = RadioField('Способ оплаты', coerce=int)