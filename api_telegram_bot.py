#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask import request
from datetime import datetime
import sqlalchemy
import json

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/bot_telegram_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apikey = db.Column(db.String(50), nullable=False)
    apisecret = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=0, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow())
    addresses = db.relationship('Address', backref='users_', lazy=True)
    
class lists_(db.Model):
    idlist = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name_list = db.Column(db.String(50), nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow())


# In[ ]:


def create_user(jsonData):
    try:
        info_user = users(
            apikey = jsonData["apikey"],
            apisecret = jsonData["apisecret"],
            email = jsonData["email"],
            status = jsonData["status"]
        )
        db.session.add(info_user)
        db.session.commit()
        return True 
    except Exception as error:
        print(error)
        return False  
    
def delete_user(jsonData):
    id = jsonData["userID"]
    user_ = users.query.filter_by(userID=id).first()
    if user_ is None:
        return False
    else:
        db.session.delete(user_)
        db.session.commit()
        return True
    
def get_users():
    all_user = []
    for u in users.query.all():
        user = {
            'userID': u.userID,
            'apikey': u.apikey,
            'apisecret': u.apisecret,
            'email': u.email,
            'status': u.status
        }
        all_user.append(json.dumps(user))
    return all_user

def get_users_by_id(jsonData):
    id = jsonData["userID"]
    u = users.query.filter_by(userID=id).first()
    if u is None:
        return False
    else:
        user = {
            'userID': u.userID,
            'apikey': u.apikey,
            'apisecret': u.apisecret,
            'email': u.email,
            'status': u.status
        }
        return json.dumps(user)
    
def get_users_by_email(jsonData):
    e = jsonData["email"]
    u = users.query.filter_by(email=e).first()
    if u is None:
        return False
    else:
        user = {
            'userID': u.userID,
            'apikey': u.apikey,
            'apisecret': u.apisecret,
            'email': u.email,
            'status': u.status
        }
        return json.dumps(user)

    
def update_user_by_id(jsonData):
    id = jsonData["userID"]
    user_ = users.query.filter_by(userID=id).first()
    print(user_)
    if user_ is None:
        return False
    else:           
        if jsonData["apikey"] is None or jsonData["apikey"] is "":
            user_.apikey = user_.apikey
        else:
            user_.apikey = jsonData["apikey"]
            
        if jsonData["apisecret"] is None or jsonData["apisecret"] is "":
            user_.apisecret = user_.apisecret
        else:
            user_.apisecret = jsonData["apisecret"]
            
        if jsonData["email"] is None or jsonData["email"] is "":
            user_.email = user_.email
        else:
            user_.email = jsonData["email"]           
        db.session.commit()
        return True

def update_user_by_email(jsonData):
    e = jsonData["email"]
    user_ = users.query.filter_by(email=e).first()
    print(user_)
    if user_ is None:
        return False
    else:            
        if jsonData["apikey"] is None or jsonData["apikey"] is "":
            user_.apikey = user_.apikey
        else:
            user_.apikey = jsonData["apikey"]
            
        if jsonData["apisecret"] is None or jsonData["apisecret"] is "":
            user_.apisecret = user_.apisecret
        else:
            user_.apisecret = jsonData["apisecret"]
            
        if jsonData["email"] is None or jsonData["email"] is "":
            user_.email = user_.email
        else:
            user_.email = jsonData["email"]           
        db.session.commit()
        return True
    
def create_list(jsonData):
        bandera = False
        try:
            for l in lists_.query.all():
                if l.name_list == jsonData["name_list"]:
                    bandera = False
                    break
                else:
                    bandera = True
            if bandera is True:
                info_list = users(
                    id_user = jsonData["id_user"],
                    name_list = jsonData["name_list"]
                )
                db.session.add(info_list)
                db.session.commit()
                return True
            else:
                return False
        except Exception as error:
            print(error)
            return False
    
def delete_list(jsonData):
    id = jsonData["idlist"]
    list_ = lists_.query.filter_by(idlist=id).first()
    if list_ is None:
        return False
    else:
        db.session.delete(list_)
        db.session.commit()
        return True
    
def get_list():
    all_lists = []
    for l in lists_.query.all():
        list_ = {
            'idlist': l.idlist,
            'id_user': l.id_user,
            'name_list': l.name_list,
        }
        all_lists.append(json.dumps(list_))
    return all_lists

def get_list_by_id(jsonData):
    id = jsonData["idlist"]
    l = lists_.query.filter_by(idlist=id).first()
    if l is None:
        return False
    else:
        list_ = {
            'idlist': l.idlist,
            'id_user': l.id_user,
            'name_list': l.name_list,
        }
        return json.dumps(list_)
    
def update_list(jsonData):
    id = jsonData["idlist"]
    list_ = lists_.query.filter_by(idlist=id).first()
    print(list_)
    if list_ is None:
        return False
    else:
        if jsonData["id_user"] is None or jsonData["id_user"] is "":
            list_.id_user = list_.id_user
        else:
            list_.id_user = jsonData["id_user"]
            
        if jsonData["name_list"] is None or jsonData["name_list"] is "":
            list_.name_list = list_.name_list
        else:
            list_.name_list = jsonData["name_list"]
                      
        db.session.commit()
        return True


# In[ ]:


@app.route("/create_user", methods=['POST'])
def create_user_():
    data = request.get_json()
    return str(create_user(data))

@app.route("/create_list", methods=['POST'])
def create_list_():
    data = request.get_json()
    return str(create_list(data))

@app.route("/delete_user", methods=['DELETE'])
def delete_user_():
    data = request.get_json()
    return str(delete_user(data))

@app.route("/delete_list", methods=['DELETE'])
def delete_list_():
    data = request.get_json()
    return str(delete_list(data))

@app.route("/get_users", methods=['GET'])
def get_users_():
    return str(get_users())

@app.route("/get_list", methods=['GET'])
def get_list_():
    return str(get_list())

@app.route("/get_users_by_id", methods=['GET'])
def get_users_by_id_():
    data = request.get_json()
    return str(get_users_by_id(data))

@app.route("/get_list_by_id", methods=['GET'])
def get_list_by_id_():
    data = request.get_json()
    return str(get_list_by_id(data))

@app.route("/get_users_by_email", methods=['GET'])
def get_users_by_email_():
    data = request.get_json()
    return str(get_users_by_email(data))

@app.route("/update_user_by_id", methods=['POST'])
def update_user_by_id_():
    data = request.get_json()
    return str(update_user_by_id(data))

@app.route("/update_list", methods=['POST'])
def update_list_():
    data = request.get_json()
    return str(update_list(data))

@app.route("/update_user_by_email", methods=['POST'])
def update_user_by_email_():
    data = request.get_json()
    return str(update_user_by_email(data))


# In[ ]:


if __name__ == "__main__":
    app.run()

