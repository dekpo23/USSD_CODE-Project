from User_Product_Data import Users, buyer
from file_info import load_product, load_user_detail
from helper_functions import option_selection, product_form, user_form, farmer_selection

def user_product():
    import json
    from pathlib import Path
    folder = Path.cwd()
    # Welcome message
    print("Welcome to AGROUSSD!")    
    
    while True:
        try:
            print("1. I am a farmer")
            print("2. I am a buyer")
            print("3. Exit")
            choice = int(input("Please select from the option above: "))
            if choice == 1:
                print(option_selection())
                choice_sel = int(input('Enter 1 for existing user and 2 for new user: '))
                if choice_sel == 1:
                    user_id = input("Please enter your ID: ")
                    folder = Path.cwd()
                    farmer_json = folder / 'farmers.json'
                    with open(farmer_json, "r", encoding="utf-8") as f:
                        farmer_details = json.load(f)
                        id_list = [farmer_info["ID"] for farmer_info in farmer_details]
                    if user_id not in id_list:
                        print(f"Invalid ID '{user_id}'! Please check again or Register as a new user.")
                    else:
                        print('Welcome Registered Farmer')
                        print('What would you like to do? \n1. View Listings.\n2. View Profile\n3. Add New Product.\n4. Exit')
                        choice = int(input("Select from the option above: "))
                        if choice == 4:
                            print("Logging out...")
                            break
                        elif choice == 1:
                            data = load_product()
                            user_ids = [prod['user_id'] for prod 
                            in data]
                            if user_id in user_ids:
                                for prod in data:
                                    if prod['user_id'] == user_id:
                                        print(prod)
                            else:
                                print("You do not have product listings yet!")
                        elif choice == 2:
                            data = load_user_detail(1)
                            ids = [user['ID'] for user in data]
                            if user_id in ids:
                                for user in data:
                                    if user['ID'] == user_id:
                                        print(user)
                            else:
                                pass
                        elif choice == 3:
                            print("1. Crops\n2. Livestock")
                            prod_cat_selection = int(input("Select from the categories above: "))
                            if prod_cat_selection == 1:
                                product_form(farmer_details, 'crops')
                                    
                            elif prod_cat_selection == 2:
                                product_form(farmer_details, 'livestock')
                            else:
                                print("Invalid choice! Try again")
                        else:
                            print("Invalid choice! Try again")
                elif choice_sel == 2:
                    user_detail = user_form()
                    if user_detail:
                        print("1. Crops\n2. Livestock")
                        prod_cat_selection = int(input("Select from the categories above: "))
                        if prod_cat_selection == 1:
                            farmer_selection(user_detail, 'crops')
                                    
                        elif prod_cat_selection == 2:
                            farmer_selection(user_detail, 'livestock')
                        else:
                            print("Invalid choice! Try again")
                    else:
                        pass
                else:
                    print("Invalid choice! Try again")            
            elif choice == 2:
                print(option_selection())
                choice_sel = int(input('Enter 1 for existing user and 2 for new user: '))
                if choice_sel == 1:
                    user_id = input("Please enter your ID: ")
                    folder = Path.cwd()
                    trader_json = folder / 'traders.json'
                    with open(trader_json, "r", encoding="utf-8") as f:
                        trader_details = json.load(f)
                        id_list = [trader_info["ID"] for trader_info in trader_details]
                    if user_id not in id_list:
                        print(f"Invalid ID '{user_id}'! Please check again or Register as a new user.")
                        continue
                    else:
                        print('Welcome Registered Trader')
                        print('What would you like to do? \n1. View Listings.\n2. View Profile\n3. Exit')
                        choice = int(input("Select from the option above: "))
                    if choice == 3:
                        print("Logging out")
                        break
                    elif choice == 2:
                        data = load_user_detail(2)
                        ids = [user['ID'] for user in data]
                        if user_id in ids:
                            for user in data:
                                if user['ID'] == user_id:
                                    print(user)
                        else:
                            pass
                        return None
                    elif choice == 1:
                        data = load_product()
                        user_data = load_user_detail(1)

                        for prod in data:
                            print(prod)
                        choice = int(input("Would you like to buy a product? 1 for yes and 2 for no"))
                        if choice == 1:
                            p_choice = input("Enter product ID")
                            p_ids = [prod['ID'] for prod in data]
                            if p_choice in p_ids:
                                for prod in data:
                                    if prod['ID'] == p_choice:
                                        print("Contact Seller:")
                                        for data in user_data:
                                            if data["ID"] == prod["user_id"]:
                                                print("Name: ", data['name'])
                                                print("Location: ", data['location'])
                                                print("Phone number: ", data['phone number'])
                        if choice == 2:
                            pass
                        print("=" * 20)
                        print("Back to Previous Menu....")
                    else:
                        print("Invalid choice. Try again!")
                elif choice_sel == 2:
                    print(option_selection())
                    user_detail = user_form()
                    if user_detail:
                        user_detail = Users(user_detail.name, user_detail.age, user_detail.gender, user_detail.location, user_detail.phone_number)
                        buyer_details = buyer(user_detail.user_id, user_detail.name, user_detail.age, user_detail.gender, user_detail.location, user_detail.phone_number)
                        buyer_details.save_info()
                        print("Registration successful!!")
                    else:
                        print("Error completing registration.. 🤔")
                else:
                    print("Invalid choice! Try again")
            elif  choice == 3:
                print("Thank you for using AGROUSSD!")
                break
        except ValueError as e:
            print('Error:', e)
        except Exception as e:
            print('Error:', e)
        
user_product()
