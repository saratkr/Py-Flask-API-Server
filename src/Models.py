from marshmallow import fields, Schema, validate
import datetime
from src.extensions import db

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.city = data.get('city')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return Users.query.all()
    
    @staticmethod
    def get_one_user(id):
        return Users.query.get(id)
    
    @staticmethod
    def get_user_by_email(email):
        return Users.query.filter_by(email=email).first()
    
    def __repr(self):
        return '<id {}>'.format(self.id)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True, validate=validate.Email(error="Invalid email address provided"))
    password = fields.Str(required=True, validate=[validate.Length(min=2, max=8)])
    city = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)