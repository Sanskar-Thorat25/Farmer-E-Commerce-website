import json
from app import create_app
from flask import g

app = create_app()
app.testing = True
with app.app_context():
    with app.test_client() as client:
        # We need a user session to access cart. 
        # Using demo_buyer: 'buyer@test.com', 'password123'
        resp = client.post('/api/login', json={'email': 'buyer@test.com', 'password': 'password123'}, follow_redirects=True)
        print("Login code:", resp.status_code)
        
        resp2 = client.get('/api/buyer/cart')
        print("Cart GET code:", resp2.status_code)
        print("Cart Data snippet:", resp2.get_data(as_text=True)[:500])
