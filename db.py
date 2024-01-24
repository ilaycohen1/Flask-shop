import sqlite3
from classes import User, Address, Review, Product, Order

DB_NAME = "project.db"

# Create Functions

def create_table(table_name, columns:str="('id' TEXT PRIMARY KEY, 'username' TEXT, 'password' TEXT)"):
    """
    Keyword arguments: table_name, columns
    table_name -- the name of the table you are creating.
    columns -- the columns of the table in the format '('column' column_type)'
    Return: this function creates a table in the db.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cur=conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {columns}")

def query(sql):
    """
    Keyword arguments: sql
    sql -- the sql query you want to execute.
    Return: this function executes the sql you type in.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql).fetchall()
    
def add_user(user:User):
    """
    Keyword arguments: user
    user -- User object
    Return: This function creates a new User to the users table.
    """
    query(f"INSERT INTO users (name, last_name, username, password, email, address_id, safety_question, safety_ans) VALUES ('{user.name}', '{user.last_name}', '{user.username}', '{user.password}', '{user.email}', '{user.address_id}', '{user.safety_question}', '{user.safety_ans}')")

def add_address(address:Address):
    """
    Keyword arguments: address
    address -- Address object
    Return: This function creates a new address in the addresses table.
    """
    query(f"INSERT INTO users (country, city, street, number, floor, apartment) VALUES ('{address.country}', '{address.city}', '{address.street}', '{address.number}', '{address.floor}', '{address.apartment}')")

def add_review(review:Review):
    """
    Keyword arguments: review
    review -- Review object
    Return: This function creates a new review in the reviews table.
    """
    query(f"INSERT INTO reviews (rating, comment, product_id) VALUES ('{review.rating}', '{review.comment}', '{review.product_id}')")

def add_product(product:Product):
    """
    Keyword arguments: product
    product -- Product object
    Return: This function creates a new product in the products table.
    """
    query(f"INSERT INTO products (name, category, price, stock, brand, ordered) VALUES ('{product.name}', '{product.category}', '{product.price}', '{product.stock}', '{product.brand}', '{product.ordered}')")

def add_order(order:Order):
    """
    Keyword arguments: order
    order -- Order object
    Return: This function creates a new order in the orders table.
    """
    query(f"INSERT INTO orders (order_date, user_id, product_id, status) VALUES ('{order.order_date}', '{order.user_id}', '{order.product_id}', '{order.status}')")


# Read Functions: 

# Address: 
def listToObjectAddress(attrListAddress):
    for a in attrListAddress:
        return Address(address_id=a[0], country=a[1], city=a[2], street=a[3], number=a[4], floor=a[5], apartment=a[6])

def listToDictAddress(attrListAddress):
    for a in attrListAddress:
        return {"address_id" : a[0], "country" : a[1], "city" : a[2], "street" : a[3], "number" : a[4], "floor" : a[5], "apartment" : a[6]}
    
def get_address_by_user(user_id):
    address_id = query(f"SELECT address_id FROM users WHERE user_id='{user_id}'")[0][0]
    address = query(f"SELECT address_id, country, city, street, number, floor, apartment FROM addresses WHERE address_id = '{address_id}'")
    return listToObjectAddress(address)

# User:

#User without sensitive information:
def listToObjectUserBasic(attrListUser):
        for u in attrListUser:
            return User(user_id=u[0], name=u[1], last_name=u[2], username=u[3], email=u[4], address_id=u[5], address=get_address_by_user(u[0]))

def listToDictUserBasic(attrListUser):
        for u in attrListUser:
            return {"user_id" : u[0], "name" : u[1], "last_name" : u[2], "username" : u[3], "email" : u[4], "address_id" : u[5], "address" : get_address_by_user(u[0]).__str__()}
    
def get_basicUser_by_id(user_id):
    user = query(f"SELECT user_id, name, last_name, username, email, address_id from users WHERE user_id='{user_id}'")
    return listToObjectUserBasic(user)

# Full User:
def listToObjectUser(attrListUser, classOrDict="class"):
    for u in attrListUser:
        return User(user_id=u[0], name=u[1], last_name=u[2], username=u[3], password=u[4], email=u[5], address_id=u[6], safety_question=u[7], safety_ans=u[8], address=get_address_by_user(u[0]))

def listToDictUser(attrListUser):
    for u in attrListUser:
        return {"user_id" : u[0], "name" : u[1], "last_name" : u[2], "username" : u[3], "password" : u[4], "email" : u[5], "address_id" : u[6], "safety_question" : u[7], "safety_ans" : u[8], "address" : get_address_by_user(u[0]).__str__()}

def get_users():
    users = query("SELECT user_id, name, last_name, username, password, email, safety_question, safety_ans, address_id  FROM users")
    return [listToObjectUser([user]) for user in users]

# Product:
def listToObjectProduct(attrListProduct):
    for p in attrListProduct:
        return Product(product_id=p[0], name=p[1], category=p[2], price=p[3], stock=p[4], brand=p[5], ordered=p[6], image=p[7])

def listToDictProduct(attrListProduct:list):
    for p in attrListProduct:
        return {"product_id" : p[0], "name" : p[1], "category" : p[2], "price" : p[3], "stock" : p[4], "brand" : p[5], "ordered" : p[6], "image" : p[7]}
        
def get_products():
    products = query("SELECT product_id, name, category, price, stock, brand, ordered, image FROM products")
    return [listToObjectProduct([p]) for p in products]

def get_products_dict():
    products = query("SELECT product_id, name, category, price, stock, brand, ordered, image FROM products")
    return [listToDictProduct([p]) for p in products]


# Order:
def listToObjectOrder(attrListOrder):
   for o in attrListOrder:
        return Order(order_id=o[0], order_date=o[1], user_id=o[2], product_id=o[3], status=o[4], address=get_address_by_user(o[2]), user=get_basicUser_by_id(o[2]), product= get_product_by_id(o[3]))

   
def listToDictOrder(attrListOrder):
    for o in attrListOrder:
        return {"order_id" : o[0], "order_date" : o[1], "user_id" : o[2], "product_id" : o[3], "status" : o[4], "address" : (get_address_by_user(o[2]).__str__()), "user" : get_basicUser_by_id(o[2]).__str__(), "product" : get_product_by_id(o[3]).__str__()}

def get_orders(classOrDict="class"):
    orders = query("SELECT order_id, order_date, user_id, product_id, status FROM orders")
    if classOrDict == "dict":
        return [listToDictOrder([o]) for o in orders]
    else:
        return [listToObjectOrder([o]) for o in orders]

# Reviews:
def listToObjectReview(attrListReview):
    for r in attrListReview:
        return Review(review_id=r[0], rating=r[1], comment=r[2], product_id=r[3], product=get_product_by_id(r[3]))        
                
def listToDictReview(attrListReview):
    for r in attrListReview:
        return {"review_id" : r[0], "rating" : r[1], "comment" : r[2], "product_id" : r[3], "product" : get_product_by_id(r[3])}

def get_reviews(classOrDict="class"):
    reviews = query("SELECT * FROM reviews")
    if classOrDict == "dict":
        return [listToDictReview([r]) for r in reviews]
    else:
        return [listToObjectReview([r]) for r in reviews]

def get_addresses():
    users = get_users()
    return [get_address_by_user(u.user_id) for u in users]

def get_reviews_by_product(product_id, classOrDict="class"):
    reviews = query(f"SELECT review_id, rating, comment, product_id FROM reviews WHERE product_id = '{product_id}'")
    if classOrDict == "dict":
        return [listToDictReview([r]) for r in reviews]
    else:
        return [listToObjectReview([r]) for r in reviews]


#----------

def get_secured_details(user_id):
    details = query(f"SELECT password, safety_question, safety_ans FROM users WHERE user_id = {user_id}")[0]
    details_dict = {'password' : details[0], 'safety_question' : details[1], 'safety_ans' : details[2]}
    return details_dict

def get_all_secured_details():
    users = get_users()
    return [get_secured_details(u.user_id) for u in users]

def get_product_categories():
    categories = query("SELECT DISTINCT category FROM products")
    return [c[0] for c in categories]

def get_product_brands():
    brands = query("SELECT DISTINCT brand FROM products")
    return [b[0] for b in brands]

def get_product_by_id(product_id, classOrDict="class"):
    product = query(f"SELECT * FROM products WHERE product_id = '{product_id}'")
    if classOrDict == "class":
        return listToObjectProduct(product)
    else:
        return listToDictProduct(product)

def get_products_by_category(category_name):
    products = query(f"SELECT * FROM products WHERE category = '{category_name}'")
    return [listToDictProduct([p]) for p in products]

def get_products_by_brand(brand_name):
    products = query(f"SELECT * FROM products WHERE brand = '{brand_name}'")
    return [listToDictProduct([p]) for p in products]

def get_products_by_price(priceOperator, priceInput):
    products = ""
    if priceOperator == "Bigger than": 
        products = query(f"SELECT * FROM products WHERE price > '{priceInput}'")       
    elif priceOperator == "Lower than":
        products = query(f"SELECT * FROM products WHERE price < '{priceInput}'")
    else:
        products = query(f"SELECT * FROM products WHERE price = '{priceInput}'")
    return [listToDictProduct([p]) for p in products]
    

def get_orders_by_product(product_name):
    product_id = query(f"SELECT product_id FROM products WHERE name = '{product_name}'")[0][0]
    orders = query(f"SELECT order_id, order_date, user_id, product_id, status FROM orders WHERE product_id = '{product_id}'")
    return [listToDictOrder([o]) for o in orders]

def get_user_by_username(username):
    user = query(f"SELECT * FROM users WHERE username='{username}'")
    return listToDictUser(user)

def sumPrice(productsIdsList):
    sum = 0
    for id in productsIdsList:
        p = get_product_by_id(id)
        sum += p.price
    return sum