import pytest

from project import create_app, db
from project.api.models import User

# fixtures are reusable objects for tests. They have scope associated with them:
#   function - once per test function
#   class - once per test class
#   module - once per test module
#   session - once per test session

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app   # testing happens here

@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db        # testing happens here
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user