import db
import classes as c
from faker import Faker
from bs4 import BeautifulSoup as bs
import requests


# db.create_table('addresses', "('address_id' INTEGER PRIMARY KEY, 'country' TEXT, 'city' TEXT, 'street' TEXT, 'number' INTEGER, 'floor' INTEGER, 'apartment' INTEGER)")
# db.create_table('users', "('user_id' INTEGER PRIMARY KEY, 'name' TEXT, 'last_name' TEXT, 'username' TEXT, 'password' TEXT, 'email' TEXT, 'address_id' INTEGER, 'safety_question' TEXT, 'safety_ans' TEXT, FOREIGN KEY ('address_id') REFERENCES addresses ('address_id'))")
# db.create_table('reviews', "('review_id' INTEGER PRIMARY KEY, 'comment' TEXT, 'rating' INTEGER, 'product_id' INTEGER, FOREIGN KEY ('product_id') REFERENCES products ('product_id'))")
# db.create_table('products', "('product_id' INTEGER PRIMARY KEY, 'name' TEXT, 'category' TEXT, 'price' INTEGER, 'stock' INTEGER, 'brand' TEXT)")
# db.create_table('orders', "('order_id' INTEGER PRIMARY KEY, 'product_id' INTEGER, 'order_date' TEXT, 'user_id' INTEGER, FOREIGN KEY ('product_id') REFERENCES products ('product_id'), FOREIGN KEY ('user_id') REFERENCES users ('user_id'))")

# response = requests.get("https://randomuser.me/api/").json()


g = db.get_address_by_user(1)
print(g)

d = db.get_secured_details(1)
print(d)

print(db.get_users())

d = db.get_all_secured_details()
print(d)