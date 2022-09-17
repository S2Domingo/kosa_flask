# -*- coding: utf-8 -*-
from datetime import datetime

import flask_login

from app import db 


class UserMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    birth = db.Column(db.DateTime, nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    alergy_dai = db.Column(db.Boolean, nullable=True)
    alergy_cru = db.Column(db.Boolean, nullable=True)
    alergy_nut = db.Column(db.Boolean, nullable=True)
    alergy_pch = db.Column(db.Boolean, nullable=True)
    role_admin = db.Column(db.Boolean, default=False)


class UserModel(UserMixin, flask_login.UserMixin, db.Model):
    __tablename__ = 'users'


class ProductMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(30))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(255))
    create_date = db.Column(db.DateTime(), nullable=False)
    product_detail = db.Column(db.Text, nullable=True)
    alergy_dai = db.Column(db.Boolean, nullable=True)
    alergy_cru = db.Column(db.Boolean, nullable=True)
    alergy_nut = db.Column(db.Boolean, nullable=True)
    alergy_pch = db.Column(db.Boolean, nullable=True)


class ProductModel(ProductMixin, db.Model):
    __tablename__ = 'products'