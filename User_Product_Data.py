class Users:
    def __init__(self, name, age, gender, location):
        self.user_id = self.generate_id()
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
    def generate_id(self):
        import random
        return 'ID' + str(random.randint(1000, 9999))
class farmer(Users):
    def __init__(self, user_id, name, age, gender, location, crop_category):
        super().__init__(name, age, gender, location)
        self.id = user_id
        self.crop_category = crop_category
        self.stock = 0
    def track_stock(self):
        pass
    def save_info(self):
        from pathlib import Path
        import json
        folder = Path.cwd()
        farmer_json = folder / 'farmers.json'
        farmer = {'ID': self.user_id, 'name': self.name, 'age': self.age, 'gender': self.gender, 'location': self.location, 'crop category': self.crop_category, 'total_stock': self.stock}
        if farmer_json.exists():
            with open(farmer_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        data.append(farmer)

        with open(farmer_json, 'w', encoding='utf-8') as f:
                json.dump(data, f)
        
    def validate_age(self, age):
        return self.age >= 18
class buyer(Users):
    def __init__(self, user_id, name, age, gender, location):
        super().__init__(name, age, gender, location)
        self.user_id = user_id
        self.amount = 0
    def track_amount(self):
        pass
    def save_info(self):
        from pathlib import Path
        import json
        folder = Path.cwd()
        trader_json = folder / 'traders.json'
        trader = {'ID': self.user_id, 'name': self.name, 'age': self.age, 'gender': self.gender, 'location': self.location, 'crop category': self.crop_category, 'Amount_sold': self.amount}
        if trader_json.exists():
            with open(trader_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        data.append(trader)
        
        with open(trader_json, 'w', encoding='utf-8') as f:
                json.dump(data, f)
        
class ProductCategory:
    def __init__(self, category_id, name, description=None, is_active=True):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]
    def get_products(self):
        return self.products
    def _str_(self):
        return f"{self.name} ({len(self.products)} items)"

class Product:
    def __init__(self, user_id, category_id, name, price, quantity, description=None):
        self.product_id = self.generate_id()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.user_id = user_id
        self.description = description
        self.category_id = category_id  

    def save_product(self):
        from pathlib import Path
        import json
        folder = Path.cwd()
        product_json = folder / 'products.json'
        product = {'ID': self.product_id, 'user_id': self.user_id, 'name': self.name, 'quantity': self.quantity, 'desciption': self.description, 'category_id': self.category_id}
        if product_json.exists():
            with open(product_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        data.append(product)
        
        with open(product_json, 'w', encoding='utf-8') as f:
                json.dump(data, f)
        
    def generate_id(self):
        import random
        return 'PRODID' + str(random.randint(1000, 9999))

    def _str_(self):
        return f"{self.name} - {self.price} NGN ({self.quantity} units)"

