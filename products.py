import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox  

# Sample product data (you can replace this with your own data)
products = []

def add_product():
    product_id = product_id_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    
    if product_id and name and price and quantity:
        products.append((product_id, name, price, quantity))
        update_table()
        
        # Clear the entry fields after adding
        product_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

def clear_entries():
    product_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def update_table():
    for i in product_tree.get_children():
        product_tree.delete(i)
    for product in products:
        product_tree.insert('', 'end', values=product)

def delete_product():
    selected_item = product_tree.selection()
    if selected_item:
        product_tree.delete(selected_item)
        products.pop(selected_item[0])

# Create the main window
root = tk.Tk()
root.title("Supermarket Products")
root.resizable(False,False)
root.geometry('900x600')
root.state('zoomed')


# Create a frame for the product details
product_frame = tk.Frame(root)
product_frame.pack(side=tk.LEFT, pady=0, padx=0)

# Create labels and text fields in pairs, one pair per line
product_id_label = tk.Label(product_frame, text="Product ID:")
product_id_label.grid(row=0, column=0, padx=10, pady=50)
product_id_entry = tk.Entry(product_frame)
product_id_entry.grid(row=0, column=1, padx=10, pady=5)

name_label = tk.Label(product_frame, text="Product Name:")
name_label.grid(row=1, column=0, padx=10, pady=65 )
name_entry = tk.Entry(product_frame)
name_entry.grid(row=1, column=1, padx=10, pady=5)

price_label = tk.Label(product_frame, text="Product Price:")
price_label.grid(row=2, column=0, padx=10, pady=65)
price_entry = tk.Entry(product_frame)
price_entry.grid(row=2, column=1, padx=10, pady=5)

quantity_label = tk.Label(product_frame, text="Product Quantity:")
quantity_label.grid(row=3, column=0, padx=10, pady=75)
quantity_entry = tk.Entry(product_frame)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=30 , padx=0)
button_frame.pack(side=tk.BOTTOM)#bg


add_button = tk.Button(button_frame, text="Add", command=add_product , padx=30 ,pady=5)#bg
clear_button = tk.Button(button_frame, text="Clear", command=clear_entries,padx=30,pady=5)#bg
delete_button = tk.Button(button_frame, text="Delete", command=delete_product,padx=30,pady=5)#bg

add_button.pack(side=tk.LEFT, padx=150 ,pady=5)
clear_button.pack(side=tk.LEFT, padx=150,pady=5)
delete_button.pack(side=tk.LEFT, padx=150,pady=5)

# Create a frame for the product table
table_frame = tk.Frame(root)
table_frame.pack(side=tk.TOP, pady=20, padx=20, fill=tk.BOTH, expand=True)

# Create a label for the product table
table_label = tk.Label(table_frame, text="Product List", font=("Helvetica", 16))
table_label.pack()

# Create a treeview table to display products
product_tree = ttk.Treeview(table_frame, columns=("Product ID", "Name", "Price", "Quantity"), show="headings")
product_tree.heading("Product ID", text="Product ID")
product_tree.heading("Name", text="Name")
product_tree.heading("Price", text="Price")
product_tree.heading("Quantity", text="Quantity")
product_tree.pack(fill=tk.BOTH, expand=True)

# Add some padding and set window size
root.geometry("800x600")
root.configure(bg='lightgray')

# Run the main loop
root.mainloop()
