from datetime import datetime
from application.models import UserModel


def create_users():
    users = [
        UserModel(
            first_name='John',
            last_name='Doe',
            cpf='369.474.310-34',
            email='john.doe@example.com',
            birth_date=datetime(1990, 1, 1)
        ),
        UserModel(
            first_name='Jane',
            last_name='Smith',
            cpf='020.044.010-10',
            email='jane.smith@example.com',
            birth_date=datetime(1985, 5, 15)
        )
    ]

    UserModel.objects().insert(users)


def clear_db_seeds():
    UserModel.objects().delete()
