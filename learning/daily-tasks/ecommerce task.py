import tkinter as tk
from tkinter import messagebox
import pyodbc
import os
from PIL import Image, ImageTk

def create_tables_if_not_exists(cursor):
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users')
    CREATE TABLE users(
        id INT PRIMARY KEY IDENTITY(1,1),
        name NVARCHAR(100) NOT NULL,
        address NVARCHAR(255),
        cart NVARCHAR(MAX)
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'products')
    CREATE TABLE products(
        id INT PRIMARY KEY IDENTITY(1,1),
        name NVARCHAR(100) NOT NULL,
        price FLOAT NOT NULL,
        url NVARCHAR(255)
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'orders')
    CREATE TABLE orders (
        id INT PRIMARY KEY IDENTITY(1,1),
        user_id INT NOT NULL,
        product_name NVARCHAR(100) NOT NULL,
        total_amount FLOAT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )""")

def sanitize_path(path):
    # Convert relative paths to absolute paths if needed
    if not os.path.isabs(path):
        return os.path.abspath(path)
    return path

def shop(cursor, products_frame, cart):
    for widget in products_frame.winfo_children():
        widget.destroy()

    cursor.execute("SELECT id, name, price, url FROM products")
    products = cursor.fetchall()

    vegetable_label = tk.Label(products_frame, text="fruit Products")
    vegetable_label.pack(pady=5)

    for product in products:
        product_frame = tk.Frame(products_frame)
        product_frame.pack(side="left", padx=5, pady=5)

        label = tk.Label(product_frame, text=f"{product[1]} - Rs {product[2]}")
        label.pack()

        img_path = sanitize_path(product[3])
        try:
            img = Image.open(img_path)
            img = img.resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(product_frame, image=photo)
            img_label.image = photo
            img_label.pack()
        except (FileNotFoundError, OSError) as e:
            print(f"Image not found for product: {product[1]}, error: {e}")

        add_to_cart_button = tk.Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(cart, p))
        add_to_cart_button.pack()

def add_to_cart(cart, product):
    item = {
        'id': product[0],
        'name': product[1],
        'price': product[2]
    }
    cart.append(item)
    messagebox.showinfo("Cart", f"{product[1]} added to cart.")

def checkout(cart):
    if not cart:
        messagebox.showinfo("Empty Cart", "Your cart is empty!")
        return

    total_amount = sum(item['price'] for item in cart)
    cart_items = "\n".join([f"Name: {item['name']}, Price: Rs {item['price']}" for item in cart])
    messagebox.showinfo("Checkout", f"Items in Cart:\n{cart_items}\nTotal Amount: Rs {total_amount}")

def buy(cursor, conn, cart):
    if not cart:
        messagebox.showinfo("Empty Cart", "Your cart is empty!")
        return

    user_id = 1  # Example user ID
    product_names = ", ".join(item['name'] for item in cart)
    total_amount = sum(item['price'] for item in cart)

    try:
        cursor.execute(
            "INSERT INTO orders (user_id, product_name, total_amount) VALUES (?, ?, ?)",
            (user_id, product_names, total_amount)
        )
        conn.commit()
        messagebox.showinfo("Order Placed", "Your order has been placed successfully!")
        cart.clear()
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"An error occurred while placing the order: {e}")

def get_orders(cursor):
    try:
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        if not orders:
            messagebox.showinfo("No Orders", "No orders found.")
            return

        orders_info = "\n".join([f"Order ID: {order[0]}, User ID: {order[1]}, Product Names: {order[2]}, Total Amount: Rs {order[3]}" for order in orders])
        messagebox.showinfo("Orders", f"Orders:\n{orders_info}")
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"An error occurred while fetching orders: {e}")

def save_user_details(cursor, conn, name_entry, address_entry):
    name = name_entry.get()
    address = address_entry.get()
    if not name:
        messagebox.showerror("Error", "Please enter a name.")
        return
    if not address:
        messagebox.showerror("Error", "Please enter an address.")
        return

    try:
        cursor.execute("INSERT INTO users (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
        messagebox.showinfo("Success", "User details saved successfully.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"An error occurred while saving user details: {e}")

root = tk.Tk()
root.title("E-Commerce Platform")

conn_str = ("Driver={ODBC Driver 17 for SQL Server};"

            "Server=SRIRAMCHEBROLU;"

            "Database=sriram;"

            "Trusted_Connection=yes;")


conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

create_tables_if_not_exists(cursor)

user_frame = tk.LabelFrame(root, text="User Details", padx=10, pady=10)
user_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(user_frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(user_frame)
name_entry.grid(row=0, column=1)

tk.Label(user_frame, text="Address:").grid(row=1, column=0)
address_entry = tk.Entry(user_frame)
address_entry.grid(row=1, column=1)

save_button = tk.Button(user_frame, text="Save", command=lambda: save_user_details(cursor, conn, name_entry, address_entry))
save_button.grid(row=2, columnspan=2, pady=10)

products_frame = tk.LabelFrame(root, text="Product Listings", padx=10, pady=10)
products_frame.grid(row=1, column=0, padx=10, pady=10)

cart_frame = tk.LabelFrame(root, text="User Cart", padx=10, pady=10)
cart_frame.grid(row=1, column=1, padx=10, pady=10)

cart = []
shop_button = tk.Button(root, text="Shop", command=lambda: shop(cursor, products_frame, cart))
shop_button.grid(row=2, column=0, pady=10)

checkout_button = tk.Button(root, text="Checkout", command=lambda: checkout(cart))
checkout_button.grid(row=2, column=1, pady=10)

buy_button = tk.Button(root, text="Buy", command=lambda: buy(cursor, conn, cart))
buy_button.grid(row=2, column=2, pady=10)

get_orders_button = tk.Button(root, text="Orders History", command=lambda: get_orders(cursor))
get_orders_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()