from flask import Blueprint

# Создаем blueprint
profile_bp = Blueprint('profile', __name__, url_prefix='/profile')
checkout_bp = Blueprint('checkout', __name__)

# Импортируем роуты ПОСЛЕ создания blueprint, не забудь!!!!!
from . import profile
from . import checkout
