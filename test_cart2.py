from app.db import get_db_connection
from app import create_app

app = create_app()
with app.app_context():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, username FROM user WHERE role='buyer' OR username='Sanskar_Thorat'")
        users = cur.fetchall()
        print("Users found:", users)
        
        if not users:
            print("No buyers found")
            exit()
            
        user_id = 3
        print("Testing for user_id:", user_id)
        
        cur.execute("""
            SELECT 
                cart_item.id as cart_id, 
                cart_item.quantity, 
                product.id as product_id, 
                product.title, 
                product.price, 
                product.stock as max_stock,
                product.image_file,
                product.unit,
                product.user_id as farmer_id
            FROM cart_item 
            JOIN product ON cart_item.product_id = product.id
            WHERE cart_item.user_id = %s
        """, (user_id,))
        cart_items = cur.fetchall()
        print("Cart Items fetched:")
        for item in cart_items:
            print({k: type(v).__name__ for k, v in item.items()})
            print(item)
