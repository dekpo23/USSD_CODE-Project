from User_Product_Data import Users, farmer, Product
import json

def option_selection():
  return '1. Existing User \n2. New user'

def farmer_selection(user_detail, cat_sel):
  farmer_details = farmer(user_detail.user_id, user_detail.name, user_detail.age, user_detail.gender, user_detail.location, user_detail.phone_number, cat_sel)

  farmer_details.save_info()

  while True:
      choice_add = int(input('Do you want to add product. Enter 1 for yes and 2 for no: '))
      if choice_add == 1:
          name = input('Enter name of product here: ')
          if name == "" and name.isdigit():
              raise ValueError("Product name must include characters and cannot be empty!")
          price = int(input('Enter price per unit here ₦: '))
          if price <= 0:
              raise ValueError("Price cannot be zero or negative number")
          quant_int = int(input('Enter quantity here: '))
          if quant_int <= 0:
              raise ValueError("Quantity cannot be zero or negative number") 
          units = input('Enter unit here(in kg, bag, basket, crates, trucks or hit enter if this doesn\'t apply)')
          quantity = f'{quant_int} {units}'
          description = input('Enter product description(optional): ')
          print("Quantity: ", quantity)
          product = Product(farmer_details.user_id, cat_sel, name, price, quantity, description)
          print("Product: ", product.product_id)
          product.save_product()
          print('Your Products have been saved')
      elif choice_add == 2:
          data = farmer.load_info()
          print(f"You have created an account with AGROUSSD successfully!...\nYour User ID is '{data[-1]['ID']}'. Please save this as you would need it to log into your account.\nTaking you to previous menu now...")
          break
      else:
          pass

def product_form(farmer_details, cat_sel):
  name = input('Enter name of product here: ')
  if name == "" and name.isdigit():
      raise ValueError("Product name must include characters and cannot be empty!")
  price = int(input('Enter price per unit here ₦: '))
  if price <= 0:
      raise ValueError("Price cannot be zero or negative number")
  quant_int = int(input('Enter quantity here: '))
  if quant_int <= 0:
      raise ValueError("Quantity cannot be zero or negative number") 
  units = input('Enter unit here(in kg, bag, basket, crates, trucks or hit enter if this doesn\'t apply)')
  quantity = f'{quant_int} {units}'
  description = input('Enter product description(optional): ')
  print("Quantity: ", quantity)
  product = Product(farmer_details.user_id, cat_sel, name, price, quantity, description)
  print("Product: ", product.product_id)
  product.save_product()
  print('Your Products have been saved')

def user_form():
  try:
      name = input("Name?: ")
      if name == "" or name.isdigit():
          raise ValueError("Name must only include characters and cannot be empty!")
      age = int(input("Age?: "))
      if age <= 0:
          raise ValueError("Age cannot be a negative number or cannot be zero")
      gender = input("Gender(Female/Male)?: ")
      if gender.lower() != "female" and gender.lower() != "male":
          raise ValueError("Gender should be Male or Female")
      else:
          gender = gender.title()
      location = input("Location?: ")
      if location == "":
          raise ValueError("Location cannot be empty!")
      phone_number = input("Phone Number?: ")
      if phone_number == "" or len(phone_number) != 11:
          raise ValueError("Phone number cannot be empty and must be 11 digits!")
      else:
          user_detail = Users(name, age, gender, location, phone_number)
          return user_detail
  except ValueError as e:
      print("Error: ", e)

def view_profile(file_path, id):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        user_details = json.load(f)
    particular_user = list(filter(lambda x: x['ID'] == id, user_details))
    particular_user_list = [f'{i}: {j}' for i, j in particular_user[0].items()]
    return '\n'.join(particular_user_list)

def update_profile(file_path, id):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        user_details = json.load(f)
    particular_user = list(filter(lambda x: x['ID'] == id, user_details))
    new_particular_user = {i: input(f'Enter {i} here: ') for i in particular_user[0].keys() if i != 'Amount_sold'}
    new_particular_user['Amount_sold'] = particular_user[0]['Amount_sold']
    user_details.remove(particular_user[0])
    user_details.append(new_particular_user)
    with open(file_path, 'w', encoding = 'utf-8') as f:
        json.dump(user_details, f, indent = 4)

import json

def order_products(file_path, name):
    with open(file_path, 'r', encoding='utf-8') as f:
        product_details = json.load(f)

    # Filter products by name
    target_products = [p for p in product_details if p['name'] == name]

    if not target_products:
        print(f"No products found with name: {name}")
        return None

    print("Choose preferred product from list below:\n")
    for idx, product in enumerate(target_products, start=1):
        details = ", ".join([f"{k}: {v}" for k, v in product.items()])
        print(f"{idx}. {details}")

    choice = int(input("\nEnter the number of the product you want to buy: "))

    if 1 <= choice <= len(target_products):
        preferred_product = target_products[choice - 1]
        print("You selected:", preferred_product)
        return preferred_product
    else:
        print("Invalid choice.")
        return None
    




        


    





