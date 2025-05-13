from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Инициализация расширений
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Конфигурация
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'ваш_секретный_ключ'  # Замените на настоящий секретный ключ

    # Инициализация расширений
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    # Регистрация blueprints
    from app.routes.main import main_bp
    from app.routes.checkout import checkout_bp
    from app.routes.profile import profile_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(profile_bp)

    # User loader
    from app.models.user import User  # Импорт после создания app

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Jinja globals
    from app.utils.messages import get_header_message
    from app.utils.titles import get_page_title

    app.jinja_env.globals.update(
        get_header_message=get_header_message,
        get_page_title=get_page_title
    )

    # Контекстный процессор
    @app.context_processor
    def inject_static():
        import os
        def file_exists(path):
            return os.path.exists(os.path.join(app.root_path, 'static', path))

        return {'file_exists': file_exists}

    return app