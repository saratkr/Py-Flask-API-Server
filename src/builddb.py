import os
from app import create_app, db
from Models import Users


USER = [
    {'name': 'Kane K', 'email': 'kkane@tm.com', 'password':'1234', 'city':'NY'},
    {'name': 'Ram Janne', 'email': 'ram@tm.com', 'password':'1234', 'city':'Delhi'},
    {'name': 'Sam Sony', 'email': 'sam@tm.com', 'password':'1234', 'city':'Delhi'},
    {'name': 'John Dare', 'email': 'john@mysite.com', 'password':'1234', 'city':'Atlanta'},
    {'name': 'Johnny Doe', 'email': 'johnny@qa.com', 'password':'1234', 'city':'Atlanta'},
    {'name': 'Jeny Jane', 'email': 'jeny1@mysite.com', 'password':'1234', 'city':'Bangalore'},
    {'name': 'Rosey De', 'email': 'rosey@dist.com', 'password':'1234', 'city':'Delhi'},
    {'name': 'Tanne Toy', 'email': 'tanne@dist.com', 'password':'1234', 'city':'Atlanta'},
    {'name': 'Myre Das', 'email': 'myre@mysite.com', 'password':'1234', 'city':'NY'},
    {'name': 'John Jane', 'email': 'jane@qa.com', 'password':'1234', 'city':'Bangalore'},
    {'name': 'Rey roy', 'email': 'rey@qa.com', 'password':'1234', 'city':'Kolkatta'},
    {'name': 'Shane Walsh', 'email': 'shane@som.com', 'password':'1234', 'city':'Austin'}
    ]

# Delete database if exists
if os.path.exists('users.db'):
    os.remove('users.db')

# Create the database
app = create_app()
with app.app_context():
    db.create_all()
    for user in USER:
        u = Users(user)
        db.session.add(u)
    db.session.commit()