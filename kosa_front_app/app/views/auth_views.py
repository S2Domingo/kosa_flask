from datetime import datetime

from flask import Blueprint, url_for, render_template, flash, request

from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserCreateForm
from app.models import UserModel

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = UserModel.query.filter_by(name=form.name.data).first()
        if not user:
            user = UserModel(name=form.name.data,
                        user_id=form.user_id.data,
                        password=generate_password_hash(form.password.data),
                        email=form.email.data,
                        create_date=datetime.now()
                        )
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('main.login'))
            
        else:
            flash('이미 존재하는 사용자입니다.')

    return render_template('auth/register.html', form=form)

# Profile
@bp.route('/detail/<int:user_id>', methods=['GET'])
def profile():
    pass

# Update 
@bp.route('/update/<int:user_id>', methods=['GET', 'POST'])
def profile_update():
    pass

# Delete
@bp.route('/delete/<int:user_id>', methods=['POST'])
def profile_delete():
    pass