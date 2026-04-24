import json
from app import create_app

app = create_app()
app.testing = True

with app.app_context():
    with app.test_client() as client:
        resp_login = client.post('/api/login', json={'email': 'buyer@test.com', 'password': 'password123'})
        print("Login status:", resp_login.status_code)
        
        # Get cart
        resp_cart = client.get('/api/buyer/cart')
        print("Cart status:", resp_cart.status_code)
        
        if resp_cart.status_code == 200:
            print("Cart payload length:", len(resp_cart.get_data()))
            # print("Cart payload:", resp_cart.get_json())
        else:
            print("Response:", resp_cart.get_data(as_text=True))
