from http import HTTPStatus


def test_get_users(client):
    cpf = '369.474.310-34'
    email = 'john.doe@example.com'

    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK

    response = client.get('/users?email=invalid_email')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert b"not exist!" in response.data

    response = client.get(f'/users?email={email}')
    assert response.status_code == HTTPStatus.OK
    assert response.json["cpf"] == cpf

    response = client.get(f'/users?cpf={cpf}')
    assert response.status_code == HTTPStatus.OK
    assert response.json["email"] == email

    response = client.get(f'/users?cpf={cpf}&email={email}')
    assert response.status_code == HTTPStatus.OK
    assert response.json["cpf"] == cpf
    assert response.json["email"] == email


def test_post_user(
    client, valid_user, user_incorrect_mask, user_less_digits, user_same_digits
):
    response = client.post('/user', json=valid_user)
    assert response.status_code == HTTPStatus.CREATED
    assert b"successfully" in response.data

    response = client.post('/user', json=valid_user)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b"CPF already exists" in response.data

    # CPF with incorrect mask
    response = client.post('/user', json=user_incorrect_mask)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b"CPF is not valid!" in response.data

    # CPF with only 10 digits
    response = client.post('/user', json=user_less_digits)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b"CPF is not valid!" in response.data

    # CPF with same digits
    response = client.post('/user', json=user_same_digits)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b"CPF is not valid!" in response.data
