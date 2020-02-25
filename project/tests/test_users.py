import json

from project.api.models import User


def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
            'username': 'thomas',
            'email': 'tom.parry@uplight.com'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'tom.parry@uplight.com was added!' in data['message']


def test_add_user_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({}),
        content_type='application/json'
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_user_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
            'email': 'tom@uplight.com'
        }),
        content_type='application/json'
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_user_duplicate_email(test_app, test_database):
    client = test_app.test_client()
    client.post(
        '/users',
        data=json.dumps({
            'username': 'thomas',
            'email': 'tom.parry@uplight.com'
        }),
        content_type='application/json'
    )
    resp = client.post(
        '/users',
        data=json.dumps({
            'username': 'thomas',
            'email': 'tom.parry@uplight.com'
        }),
        content_type='application/json'
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Sorry. That email already exists.' in data['message']


def test_single_user(test_app, test_database, add_user):
    user = add_user('gabe', 'gabe@uplight.com')
    client = test_app.test_client()
    resp = client.get(f'/users/{user.id}')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'gabe' in data['username']
    assert 'gabe@uplight.com' in data['email']


def test_single_user_incorrect_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get('/users/999')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert 'User 999 does not exist' in data['message']


def test_all_users(test_app, test_database, add_user):
    # clean database for test
    test_database.session.query(User).delete()
    add_user('thomas', 'tom.parry@uplight.com')
    add_user('gabe', 'gabe.walford@uplight.com')
    client = test_app.test_client()
    resp = client.get('/users')
    data = json.loads(resp.data.decode())
    print(data)
    assert resp.status_code == 200
    assert len(data) == 2
    assert 'thomas' in data[0]['username']
    assert 'tom.parry@uplight.com' in data[0]['email']
    assert 'gabe' in data[1]['username']
    assert 'gabe.walford@uplight.com' in data[1]['email']
