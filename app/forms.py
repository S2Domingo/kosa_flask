from socketserver import DatagramRequestHandler
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# User Register
class UserCreateForm(FlaskForm):
    name = StringField('사용자 이름', validators=[DataRequired(), Length(min=2, max=20)])
    user_id = StringField('사용자 ID', validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password_confirm', '비밀번호가 일치하지 않습니다')])
    password_confirm = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


# User Login
class UserLoginForm(FlaskForm):
    user_id = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


# User Update (password change) - no implement
class UserUpdateForm(FlaskForm):
    password = PasswordField('현재 비밀번호', validators=[DataRequired()])
    new_password = PasswordField('새로운 비밀번호', validators=[
        DataRequired(), EqualTo('new_password', '비밀번호가 일치하지 않습니다.')
    ])
    new_password_confirm = PasswordField('비밀번호 확인', validators=[DataRequired()])


# Product Create  - no implement
class ProductCreateForm(FlaskForm):
    product_name = StringField('상품 이름', validators=[DataRequired()])
    price = StringField('상품 가격', validators=[DataRequired()])
    image = FileField('상품이미지', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, '이미지만 가능합니다.')])
    submit = SubmitField('상품 등록')


