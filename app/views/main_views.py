from glob import escape
import os
#import redis

from urllib import request
from flask import Blueprint, render_template, request, session, flash, url_for, g

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app import db 
from app.models import UserModel
from app.forms import UserLoginForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('id')
    if user_id is None:
        g.user = None
    else:
        g.user = UserModel.query.get(user_id)


# @bp.route('/hello')
# def hello_pybo():
#     if 'id' in session:
#         print("get in")
#         test = escape(session[id])

#         print(test, type(test))

#         user_id = UserModel.query.get(test)

#         store = SessionStore(user_id, REDIS_URL)

#         visits = store.incr('visits')
        
#         return '''
#             Logged in as {0}.<br>
#             Visits : {1}
#         '''.format(user_id, visits)
    
#     return "Hello World!"

@bp.route('/')
def index():
        
    return render_template('index.html')

# @bp.route('/login', methods=['GET', 'POST'])
# def login():

#     form = UserLoginForm()

#     if request.method == 'POST' and form.validate_on_submit():
#         error = None 
#         user =  UserModel.query.filter_by(user_id=form.user_id.data).first()
#         if not user:
#             error = "존재하지 않는 사용자입니다."
#         elif not check_password_hash(user.password, form.password.data):
#             error = "비밀번호가 올바르지 않습니다."
#         if error is None:
#             session.clear()
#             session['id'] = user.id
#             return redirect(url_for('main.index'))
#         flash(error)
    
#     return render_template('login.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():

    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None 
        user =  UserModel.query.filter_by(user_id=form.user_id.data).first()
        print(user, type(user))
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['id'] = user.id
           
            return redirect(url_for('main.index'))

        flash(error)
    
    return render_template('login.html', form=form)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

