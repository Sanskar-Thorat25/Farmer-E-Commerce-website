import json
from app import create_app
from app.models import User
from flask_login import login_user
from app.routes.buyer import view_cart
from flask import request, current_app

app = create_app()
app.testing = True

with app.app_context():
    with app.test_request_context('/api/buyer/cart'):
        user = User(
            id=3,
            username='Sanskar_Thorat',
            email='sanskar@gmail.com',
            password='',
            role='buyer',
            image_file='default.jpg'
        )
        login_user(user)

        try:
            resp, status = view_cart()
            if status != 200:
                print("Error Status:", status)
                print(resp.get_data(as_text=True))
            else:
                print("Cart Success")
                print("Data length:", len(resp.get_data(as_text=True)))
        except Exception as e:
            import traceback
            traceback.print_exc()
