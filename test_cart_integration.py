import json
from app import create_app
from app.models import User
from flask_login import login_user

app = create_app()
app.testing = True

with app.app_context():
    with app.test_client() as client:
        # Instead of going through auth route, we can log in right inside the request context
        with client.session_transaction() as sess:
            # We must trick Flask login or just use the real API with cookies saved
            pass
        
        resp_login = client.post('/api/login', json={'email': 'sanskar@gmail.com', 'password': '123'})
        print("Login status:", resp_login.status_code)
        
        resp_cart = client.get('/api/buyer/cart')
        print("Cart status:", resp_cart.status_code)
        
        if resp_cart.status_code == 200:
            print("Cart valid")
        else:
            print("Cart Error Content:", resp_cart.get_data(as_text=True))
