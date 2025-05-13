from app import create_app
from app.models import db, User, Order

app = create_app()

with app.app_context():
    # Создаем тестового пользователя
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        phone="1234567890",
        password="password123"
    )
    db.session.add(user)
    db.session.commit()

    # Создаем тестовый заказ
    order = Order(
        user_id=user.id,
        status='pending',
        total_amount=100.0,
        shipping_address='Test Address'
    )
    db.session.add(order)
    db.session.commit()

    print("Тестовые данные созданы!")