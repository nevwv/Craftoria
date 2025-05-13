from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    # Создаём таблицы
    db.create_all()

    # Проверяем, есть ли уже пользователи
    if not User.query.first():
        test_user = User(
            first_name="Мастер",
            last_name="Рукоделия",
            email="master@example.com",
            phone="+79123456789"
        )
        test_user.password = "test123"  # Используем сеттер для безопасного хранения
        db.session.add(test_user)
        db.session.commit()
        print("✅ Тестовый пользователь создан!")
    else:
        print("ℹ️ База данных уже инициализирована")