from flask import Flask, session, request , render_template, redirect, jsonify
import requests
import db
from classes import User

app = Flask(__name__)
app.secret_key="xvklsdoiisdfjhsdfklksdflsdfkjhsdkjjsdfkjh"

log = False


@app.route('/')
def home():
    if "username" in session:
        if  session["username"] == 'admin':
           return redirect ("/admin")
        else:
            categories = db.get_product_categories()
            brands = db.get_product_brands()
            products = db.get_products_dict()
            priceOperator = ["Bigger than", "Lower than", "Equal to"]
            return render_template("shop.html", categories=categories, brands=brands, products=products, priceOperator=priceOperator)
    else:
        return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == "POST":
       username=request.form['username']
       password=request.form['password']
       if len(db.query(f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'")) > 0:
            session["username"] = request.form['username']
            return redirect("/") 
       else:                   
           return redirect("/login")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/admin')
def admin():
    if session["username"] == "admin":
        return render_template("admin.html")
    else:
        return redirect("/")
    
@app.route('/admin/users_manager')
def adminUsers():
    if session["username"] == "admin":
        return render_template("usersManager.html", users=db.get_users(), securedDetails=db.get_all_secured_details())
    else:
        return redirect("/")

@app.route('/admin/users_manager/secured_details/<user_id>')
def getSecuredDetails(user_id):
    details = db.get_secured_details(user_id)
    return jsonify(details)

@app.route('/admin/products_manager')
def adminProducts():
    if session["username"] == "admin":
        categories = db.get_product_categories()
        brands = db.get_product_brands()
        products = db.get_products_dict()
        priceOperator = ["Bigger than", "Lower than", "Equal to"]
        return render_template("productsManager.html", categories=categories, products=products, brands=brands, priceOperator=priceOperator)
    else:
        return redirect("/")
    
@app.route('/admin/products_manager/all')
def adminAllProducts():
        products = db.get_products_dict()
        return jsonify(products=products)

@app.route('/admin/products_manager/category/<selected_category>')
def productSelectCategory(selected_category):
    products = db.get_products_by_category(selected_category)
    return jsonify(products)

@app.route('/admin/products_manager/brand/<selected_brand>')
def productSelectBrand(selected_brand):
    products = db.get_products_by_brand(selected_brand)
    return jsonify(products)

@app.route('/admin/products_manager/price/<priceOperator>/<priceInput>')
def productSelectPrice(priceOperator, priceInput):
    products = db.get_products_by_price(priceOperator=priceOperator, priceInput=priceInput)
    return jsonify(products)
    
@app.route('/admin/orders_manager')
def adminOrders():
    if session["username"] == "admin":
        orders=db.get_orders()
        products = db.get_products()
        return render_template("ordersManager.html", orders=orders, products=products)
    else:
        return redirect("/")
    
@app.route('/admin/orders_manager/all')
def adminAllOrders():
    if session["username"] == "admin":
        orders=db.get_orders(classOrDict="dict")
        return jsonify(orders)
    else:
        return redirect("/")
    
@app.route('/admin/orders_manager/product/<selected_product>')
def orderSelectProduct(selected_product):
    orders = db.get_orders_by_product(selected_product)
    return jsonify(orders)

@app.route('/user/add', methods=['GET','POST'])
def addUser():
    message = "Enter your details:"
    if request.method == 'POST':
        values = list(request.form.to_dict().values())
        user = db.listToObjectUser([values])
        db.add_user(user)
        message = f"Thanks For Joining!\nNew User Added:\n{user}"
        return render_template("signup.html", message=message)
    else:
        return render_template("signup.html", message=message)
    

@app.route('/forgotPassword/<username>')
def forgot(username):
    user = db.get_user_by_username(username)
    return jsonify(user)
 
@app.route('/products/all')
def allProducts():
    products = db.get_products_dict()
    return jsonify(products=products) 
        
@app.route('/products/category/<selected_category>')
def productByCategory(selected_category):
    products = db.get_products_by_category(selected_category)
    return jsonify(products)

@app.route('/products/brand/<selected_brand>')
def productByBrand(selected_brand):
    products = db.get_products_by_brand(selected_brand)
    return jsonify(products)

@app.route('/products/price/<priceOperator>/<priceInput>')
def productByPrice(priceOperator, priceInput):
    products = db.get_products_by_price(priceOperator=priceOperator, priceInput=priceInput)
    return jsonify(products)

@app.route('/cart/add/<productID>')
def addToCart(productID):
    cart = session["cart"]
    cart.append(productID)
    session["cart"] = cart
    message = {"messageAdd" : "Added to cart"}
    return jsonify(message)

