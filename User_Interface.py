


def option_selection():
    return '1. Existing User \n2. New user'

def user_product():
    import json
    from pathlib import Path
    folder = Path.cwd()
    while True:
        # Welcome message
        print("Welcome to AGROUSSD!")    
        print("1. I am a farmer")
        print("2. I am a buyer")
        print("3. Exit")


        try:
            choice = int(input("Please select from the option above: "))
            if choice == 1:
                print(option_selection())
                choice_sel = int(input('Enter 1 for existing user and 2 for new user '))
                if choice_sel == 1:
                    user_id = input("Please enter your ID: ")
                    folder = Path.cwd()
                    farmer_json = folder / 'farmers.json'
                    with open(farmer_json, "r", encoding="utf-8") as f:
                        farmer_details = json.load(f)
                    for farmer_info in farmer_details:
                        if user_id == farmer_info["ID"]:
                            print('Welcome Registered Farmer')
                            
            
                elif choice_sel == 2:
                    print(option_selection())
                    name = input("Name?: ")
                    age = int(input("Age?: "))
                    gender = input("Gender(Female/Male?: ")
                    location = input("Location?: ")
                    user_detail = Users(name, age, gender, location)
                    id = user_detail.generate_id()
                    print("1. Crops\n2. Livestock")
                    crop_cat_selection = int(input("Select from the categories above: "))
                    if crop_cat_selection == 1:
                        farmer_details = farmer(id, name, age, gender, location, 'crops')
                        farmer_details.save_info()
                        while True:
                            choice_add = int(input('Do you want to add product. Enter 1 for yes and 2 for no'))
                            if choice_add == 1:
                                name = input('Enter name of product here: ')
                                price = int(input('Enter price per unit here ₦: '))
                                quant_int = int(input('Enter quantity here: '))
                                units = input('Enter unit here(in kg, bag, basket)')
                                category_id = 'C001'
                                quantity = f'{quant_int} {units}'
                                product = Product(id, category_id, name, price, quantity)
                                product.save_product()
                                print('Your Products have been saved')
                            elif choice_add == 2:
                                print('Taking you to previous menu now')
                                break
                            else:
                                pass
                            
                        
                    elif crop_cat_selection == 2:
                        user_detail = Users(name, age, gender, location)
                        id = user_detail.generate_id()
                        farmer_details = farmer(id, name, age, gender, location, 'livestocks')
                        farmer_details.save_info()
                        while True:
                            choice_add = int(input('Do you want to add product. Enter 1 for yes and 2 for no'))
                            if choice_add == 1:
                                name = input('Enter name of product here: ')
                                price = int(input('Enter price per unit here ₦: '))
                                quant_int = int(input('Enter quantity here: '))
                                units = input('Enter unit here(in crates, trucks or hit enter if this doesn\'t apply)')
                                category_id = 'A001'
                                quantity = f'{quant_int} {units}'
                                product = Product(id, category_id, name, price, quantity)
                                product.save_product()
                                print('Your Products have been saved')
                            elif choice_add == 2:
                                print('Taking you to previous menu now')
                                break
                            else:
                                pass
                            
            elif choice == 2:
                print(option_selection())
                choice_sel = int(input('Enter 1 for existing user and 2 for new user'))
                if choice_sel == 1:
                    pass
                elif choice_sel == 2:
                    print(option_selection())
                    name = input("Name?: ")
                    age = int(input("Age?: "))
                    gender = input("Gender(Female/Male?: ")
                    location = input("Location?: ")
                    id = user_detail.generate_id()
                    user_detail = Users(name, age, gender, location)
                    buyer_details = buyer(id, name, age, gender, location)
                    buyer_details.save_info()
            elif  choice == 3:
                break
        except ValueError as e:
            print('Error:', e)
        except Exception as e:
            print('Error:', e)
        


user_product()