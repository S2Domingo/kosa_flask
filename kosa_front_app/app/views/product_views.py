import os
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

from datetime import datetime

from flask import Blueprint, render_template, flash, request, url_for

from werkzeug.utils import redirect, secure_filename

from app import db
from app.models import ProductModel
from app.forms import ProductCreateForm

# SERVICE_NAME = os.environ.get('SERVICE_NAME')
# REGION_NAME  = os.environ.get('REGION_NAME')
# AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
# BUCKET_NAME = os.environ.get('BUCKET_NAME')

# # session = boto3.Session(
# #     region_name = REGION_NAME,
# #     aws_access_key_id = AWS_ACCESS_KEY,
# #     aws_secret_access_key = AWS_SECRET_KEY
# # )

# # s3 = session.client(
# #     SERVICE_NAME
# #     )

# s3 = boto3.client(
#     service_name = SERVICE_NAME,
#     region_name = REGION_NAME,
#     aws_access_key_id = AWS_ACCESS_KEY,
#     aws_secret_access_key = AWS_SECRET_KEY
# )

bp = Blueprint('product', __name__, url_prefix='/product')

#UPLOAD_FOLDER = '/path/to/the/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# 이미지 업로드 https://stackoverflow.com/questions/44926465/upload-image-in-flask

# 상품 리스트
# @bp.route('/list/', methods=['GET'])
# def list():
#     product_list = ProductModel.query.order_by(ProductModel.create_date.desc())
#     return render_template('product/product_list.html', product_list=product_list)

@bp.route('/list', methods=['GET'])
def list():
    return render_template("product/product_list.html")


# # 상품 등록 create
# @bp.route('/create', methods=['GET', 'POST'])
# def create():
#     form = ProductCreateForm()
#     if request.method == "POST" and form.validate_on_submit():
#         product_name = ProductModel.query.filter_by(product_name=form.product_name.data).first()
#         if not product_name:

#             image = form.image.data

#             try:
#                 s3.upload_fileobj(
#                 image,
#                 os.getenv("BUCKET_NAME"),
#                 image.filename,
#                 ExtraArgs={
#                     "ContentType": image.content_type
#                 }
#             )

#             except Exception as e:
#                 # This is a catch all exception, edit this part to fit your needs.
#                 print("Something Happened: ", e)
#                 return e

#             # image = form.image.data
#             # print(type(image))
#             # file_name = secure_filename(image.filename)
#             # print(image.filename)
#             # upload(image.filename)
#             file_name = secure_filename(image.filename)

#             product = ProductModel(
#                 product_name=form.product_name.data, 
#                 price=form.price.data,
#                 image_url=file_name,
#                 create_date=datetime.now()
#                 )

#             db.session.add(product)
#             db.session.commit()

#             return redirect(url_for('product.create'))

#         else:
#             flash('중복된 상품명입니다.')

#     return render_template('product/product_create.html', form=form)

# 상품 상세정보 read
@bp.route('/detail/<int:product_id>/')
def detail(product_id):
    product = ProductModel.query.get_or_404(product_id)
    return render_template('product/product_detail.html', product=product) 

# 상품 가격 변경
@bp.route('/price/<int:product_id>')
def price(product_id):
    pass

# 상품 수정 update
@bp.route('/update/<int:product_id>')
def update(product_id):
    pass

# 상품 삭제 delete
@bp.route('/delete/<int:product_id>')
def delete(product_id):
    pass

