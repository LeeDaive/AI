from extension.ext_database import db

class Auth(db.Model):
    __tablename__ = 'Auth'
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))