-- Krishi-Hub MySQL Database Creation Script
-- Run this script in MySQL Workbench or via the command line to create the database schema

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS krishi_hub_db;
USE krishi_hub_db;

-- Disable constraint checks temporarily for a clean creation/drop cycle
SET FOREIGN_KEY_CHECKS=0;

-- Optional: Drop existing tables if you are refreshing the database
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS cart_item;
DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS `order`;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS user;

-- 2. Users Table (Farmers and Buyers)
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    image_file VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    password VARCHAR(60) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'buyer' -- 'farmer' or 'buyer'
);

-- 3. Products Table (Listings uploaded by Farmers)
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    date_posted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    unit VARCHAR(20) NOT NULL DEFAULT 'kg',
    category VARCHAR(50) NOT NULL,
    image_file VARCHAR(20) NOT NULL DEFAULT 'default_product.jpg',
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

-- 4. Cart Items Table (Temporary storage for Buyers)
CREATE TABLE cart_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL DEFAULT 1,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);

-- 5. Orders Table (Checkout record for Buyers)
CREATE TABLE `order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_ordered DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending', -- Pending, Processing, Shipped, Delivered, Cancelled
    total_amount FLOAT NOT NULL,
    payment_method VARCHAR(50) NOT NULL DEFAULT 'Cash on Delivery',
    shipping_address TEXT NOT NULL,
    buyer_id INT NOT NULL,
    FOREIGN KEY (buyer_id) REFERENCES user(id) ON DELETE RESTRICT
);

-- 6. Order Items Table (Snapshot of products in an order at the time of purchase)
CREATE TABLE order_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL DEFAULT 1,
    price_at_purchase FLOAT NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `order`(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE RESTRICT
);

-- Re-enable constraint checks
SET FOREIGN_KEY_CHECKS=1;

-- 7. (Optional) Insert Dummy Data for immediate testing

-- Insert a Dummy Farmer (password is 'password123' hashed with bcrypt)
INSERT INTO user (username, email, password, role) 
VALUES ('demo_farmer', 'farmer@test.com', '$2b$12$eR/P51S/T7f4X42u9wI1gOH9WpA.3OItiR1U8zVlInO2C226dMyOS', 'farmer');

-- Insert a Dummy Buyer
INSERT INTO user (username, email, password, role) 
VALUES ('demo_buyer', 'buyer@test.com', '$2b$12$eR/P51S/T7f4X42u9wI1gOH9WpA.3OItiR1U8zVlInO2C226dMyOS', 'buyer');

-- Insert a Dummy Product (linked to user_id 1, the demo_farmer)
INSERT INTO product (title, description, price, stock, category, user_id)
VALUES ('Organic Tomatoes', 'Fresh locally grown tomatoes.', 40.0, 50, 'Vegetables', 1);
