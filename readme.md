## API server for testing/exploring Rest API.

**DB used is SQLITE, and JWT for token based authentication, the default username/password hardcoded is admin/admin**
*Tested only in Windows 10. Will work in Linux servers with minor modifications.*

**How to Use:**
1. Install python 3.6.3 if not yet done.
1. Download or clone the repo.
1. cd into the folder (Py-Flask-API-Server)
1. Install python virtual env, e.g. C:\code\Py-Flask-API-Server>virtualenv apiserveenv
1. Activate the virtual env, e.g. C:\code\Py-Flask-API-Server>apiserveenv\Scripts\activate
1. Install the required libraries, pip install -r requirements.txt
1. Run the application, python run.py

Hit the URL from any browser: http://127.0.0.1:5000/api/v1/users/test

And you should see as:

{
  "message": "Connected fine"
}

**Test Endpoints**:
* Login API: POST /api/v1/users/login

username/password is admin/admin.

Request:

{
    "username": "admin",
    "password":"admin"
}

Response for above will be:

    {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzcxMjIzMDgsIm5iZiI6MTU3NzEyMjMwOCwianRpIjoiMzJhY2NiYjEtNTgwMi00MGE3LWJiZjItNmUyN2QwOGRkMmIzIiwiZXhwIjoxNTc3MjA4NzA4LCJpZGVudGl0eSI6eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.aJot1MU5qcB72Gkgp2kJqqRtzysd32BnPbuTV_dSSNw"
    }

Use this Authorization Bearer in header for all the subsequent API's.

* Create new User: POST /api/v1/users/create

Request:

      {
        "name": "Rey1",
        "email": "rey1@qa.com",
        "password":"admin",
        "city": "Bangalore"
        }

* Get all users: GET /api/v1/users/getusers
* Get one user with ID: GET /api/v1/users/1
* Delete one user with ID: DELETE /api/v1/users/delete/2
* Delete one user with email: DELETE /api/v1/users/delete


    Request:
    {
    "email" : "rey1@qa.com"
    }

* Update one user: UPDATE /api/v1/users/update


    Request:
    {
    "name": "Rey1",
    "email": "rey1@qa.com",
    "password":"123",
    "city": "NEW DELHI"
    }

**Notes**:
users.db is included, which have ~12 entries.
If ever you need to clean/clear the DB and re-create, follow the below:

 1. cd C:\code\Py-Flask-API-Server
 1. Activate the virtual env, e.g. C:\code\Py-Flask-API-Server>apiserveenv\Scripts\activate
 1. Run the command  from inside src: e.g. C:\code\Py-Flask-API-Server\src>python buildb.py

