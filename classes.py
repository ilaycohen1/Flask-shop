
from datetime import date

class Address:
    def __init__(self, address_id=-1, country:str="", city:str="", street:str="", number:int=None, floor:int=None, apartment:int=None):
        self.address_id = address_id
        self.country = country
        self.city = city
        self.street = street
        self.number = number
        self.floor = floor
        self.apartment = apartment

    def __str__(self):
        if self.floor == None and self.apartment == None:
            return f"{self.country}, {self.city}, {self.street} {self.number}"
        else:
            return f"{self.country}, {self.city}, {self.street} {self.number}, Floor: {self.floor}, Apartment: {self.apartment}"

class User:
    def __init__(self, user_id=-1, name:str="", last_name:str="", username:str="", password:str="", email:str=None, safety_question="", safety_ans="", address_id:int=None, address:Address=None):
        self.user_id = user_id
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.safety_question = safety_question
        self.safety_ans = safety_ans
        self.address_id = address_id
        self.address=address
    
    def __str__(self):
        return f"{self.name} {self.last_name}\n{self.email}"


class Product:
    def __init__(self, product_id=-1, name:str="", category:str="", price:int=0, stock:int=0, brand:str=None, ordered:int=0, image:str=None):
        self.product_id=product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.brand = brand
        self.ordered = ordered
        self.image = image

    def __str__(self):
        return f"{self.name}\n{self.brand}"

class Review:
    def __init__(self, review_id= -1, rating:int=None, comment:str="", product_id:int=0, product:Product=None):
        self.review_id = review_id
        self.rating = rating
        self.comment = comment
        self.product_id = product_id
        self.product = product


class Order:
    def __init__(self, order_id=-1, product_id=0, product:Product=None, order_date=str(date.today()), user_id:str=0, user:User=None, address:Address=None, status:str=None):
        self.order_id=order_id
        self.order_date=order_date
        self.user_id=user_id
        self.product_id = product_id
        self.product= product
        self.user = user
        self.address = address
        self.status = status




