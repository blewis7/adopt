from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

db = SQLAlchemy()

DEFAULT_PICTURE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"


class Pet(db.Model):
    '''Pets to adopt'''

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or DEFAULT_PICTURE


def connect_db(app):
    '''Connect to database.'''

    db.app = app
    db.init_app(app)