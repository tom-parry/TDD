import sys

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

# create FlaskGroup instance to extend normal CLI with commands related to Flask app
app = create_app()
cli = FlaskGroup(create_app=create_app)

# register new command recreate_db to CLI
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='tom-parry', email="tom.parry@uplight.com"))
    db.session.add(User(username='gwalford', email="gabe.walford@uplight.com"))
    db.session.commit()

if __name__ == '__main__':
    cli()