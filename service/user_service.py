from flask import jsonify

from extension.ext_database import db
from models.user import User


def add(user):
    db.session.add(user)
    db.session.commit()


def query(id):
    return User.query.filter_by(id = id).first()
