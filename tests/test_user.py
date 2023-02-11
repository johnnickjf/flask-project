from src.models.user import User


def test_create_user():
    user = User({'username': 'joao', 'email': 'testandoja11@gmail.com', 'password': 'senha123'})
    assert user.name == 'Joao'
