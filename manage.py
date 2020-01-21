from flask.cli import FlaskGroup
from project import app, db

# create FlaskGroup instance to extend normal CLI with commands related to Flask app
cli = FlaskGroup(app)

# register new command recreate_db to CLI
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()