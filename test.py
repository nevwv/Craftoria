from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from app.models import Order
        print("Все заказы:", Order.query.all())