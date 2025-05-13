from app import create_app, db

app = create_app()

with app.app_context():
    print("Существующие таблицы:", db.engine.table_names())