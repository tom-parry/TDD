from flask.cli import FlaskGroup
from project import app

# create FlaskGroup instance to extend normal CLI with commands related to Flask app
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()