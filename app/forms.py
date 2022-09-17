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

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # product_name = db.Column(db.String(30))
    # price = db.Column(db.Integer)
    # image_url = db.Column(db.String(255))
    # create_date = db.Column(db.DateTime(), nullable=False)
    # product_detail = db.Column(db.Text)
    # alergy_dai = db.Column(db.Boolean, nullable=True)
    # alergy_cru = db.Column(db.Boolean, nullable=True)
    # alergy_nut = db.Column(db.Boolean, nullable=True)
    # alergy_pch = db.Column(db.Boolean, nullable=True)

# FileUpload https://flask-wtf.readthedocs.io/en/0.15.x/form/

# class UploadForm(FlaskForm):
#     photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
#     submit = SubmitField('Upload')


# Product Create  - no implement
class ProductCreateForm(FlaskForm):
    product_name = StringField('상품 이름', validators=[DataRequired()])
    price = StringField('상품 가격', validators=[DataRequired()])
    image = FileField('상품이미지', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, '이미지만 가능합니다.')])
    submit = SubmitField('상품 등록')


# Product Update (상품정보)  - no implement
class ProductUpdateForm(FlaskForm):
    pass

