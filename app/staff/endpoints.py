from flask import Blueprint, request

from app.staff.model import Staff


staff = Blueprint('staff', __name__, url_prefix='/staff')

@staff.post('/register')
def register_staff():
    name = request.json.get('name')
    title = request.json.get('title')
    phone = request.json.get('phone')
    email = request.json.get('email')
    avaibility = request.json.get('avaibility')
    password = request.json.get('password')

    request = Staff.get_staff_by_email_or_phone(phone=phone, email=email)
    if not request:
        Staff.create(name, title, phone, email, avaibility, password)
        return 'Account created successfully', 200
    return 'Account creation failed, please try again', 400

@staff.post('/login')
def staff_login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = Staff.get_staff_by_email(email)
    if user and user.is_valid_password(password):
        return 'Login succcessful', 200
    return 'Invalid Email or Password', 400