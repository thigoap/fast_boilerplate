from http import HTTPStatus


def test_create_user_empty_string_400(client):
    response = client.post(
        '/users',
        json={
            'username': '',
            'email': 'email@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Empty string'}
