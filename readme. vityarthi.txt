Online Pet Food Ordering System

Online Pet Food Ordering & Data Visualization

Project Overview

This project is a Python + MySQL-based application designed for managing an online pet food ordering platform.
It stores customer details, pet shop details, menu, orders, payments, ratings and more.
The project also includes data visualization using Matplotlib (bar chart, line chart, scatter plot, etc.).

This project connects problem solving, Python programming, MySQL database, algorithms, real-world domain understanding, and data visualization.


---

Objectives

Identify a real-world problem (pet food ordering)

Apply Python programming concepts

Use modular & top-down design

Create and manage database tables using MySQL

Perform CRUD operations

Display insights using graphs

Connect theory with real-world application



---

Features

Customer Module

Add Customer

View Customers


Pet Shop Module

Add Pet Shop

View Pet Shops


Orders Module

Create Order

View Orders


Ratings & Payment Module

Add Rating

Add Payment Details

View Payment Records


Data Visualization

Total Purchase per Pet Shop (Line Graph)

Shop Ratings (Bar Chart)

Menu Pricing (Line Plot)

Payment Methods (Scatter Plot)



---

Installation & Setup

Install Python

Download Python 3.10+:
https://www.python.org/downloads/

Install MySQL

Download MySQL Server + Workbench:
https://dev.mysql.com/downloads/installer/

Default credentials:

Username: root

Password: (your password)

Port: 3306


Install Required Libraries

Run in terminal:

pip install mysql-connector-python
pip install matplotlib


---

Create MySQL Database

Run these commands in MySQL Workbench:

CREATE DATABASE ofos;
USE ofos;

Create Tables

Users Table

CREATE TABLE users (
user_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255),
email VARCHAR(255) UNIQUE,
password VARCHAR(255),
phone VARCHAR(20)
);

Pet Shop Table

CREATE TABLE petshop (
petshop_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255),
address VARCHAR(255)
);

Orders Table

CREATE TABLE orders (
order_id INT PRIMARY KEY AUTO_INCREMENT,
petshop_id INT,
user_id INT,
order_total INT,
FOREIGN KEY (petshop_id) REFERENCES petshop(petshop_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

Rating Table

CREATE TABLE rating (
rating_id INT PRIMARY KEY AUTO_INCREMENT,
petshop_id INT,
rating INT,
FOREIGN KEY (petshop_id) REFERENCES petshop(petshop_id)
);

Payment Table

CREATE TABLE payment (
payment_id INT PRIMARY KEY AUTO_INCREMENT,
payment_method VARCHAR(50),
amount INT
);

Menu Table

CREATE TABLE menu (
item_id INT PRIMARY KEY AUTO_INCREMENT,
item_name VARCHAR(100),
price INT
);


---

How to Run the Project

In VS Code Terminal:

python main.py

You will see a menu like:

PET FOOD ORDERING SYSTEM MENU

1. Add Customer


2. View Customers


3. Add Pet Shop


4. View Pet Shops


5. Create Order


6. View Orders


7. View Charts


8. Exit




---

Data Visualization (Python)

Example Graph Code (Total Purchase)

import mysql.connector as m
import matplotlib.pyplot as plt

db = m.connect(host="localhost", user="root", password="sa123", database="ofos")
cursor = db.cursor()

cursor.execute("SELECT petshop.name, SUM(orders.order_total) FROM petshop INNER JOIN orders ON petshop.petshop_id = orders.petshop_id GROUP BY petshop.name")

names = []
totals = []

for row in cursor:
    names.append(row[0])
    totals.append(row[1])

plt.xlabel("Pet Shop")
plt.ylabel("Total Purchase")
plt.title("Total Purchase per Pet Shop")
plt.plot(names, totals, linestyle="dashed")
plt.show()


---

