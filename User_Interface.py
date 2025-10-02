from User_Product_Data import Users, buyer
from file_info import load_product, load_user_detail
from helper_functions import option_selection, product_form, user_form, farmer_selection, view_profile, update_profile, order_products
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
                while True:
                    print(option_selection())
                    choice_sel = int(input('Please enter choice here: '))
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
                            print('What would you like to do? \n1. View Listings.\n2. View Profile\n3. Add New Product.\n4. Back')
                            choice = int(input("Select from the option above: "))
                            if choice == 4:
                                break
                            elif choice == 1:
                                data = load_product()
                                user_ids = [prod['user_id'] for prod
                                in data]
                                if user_id in user_ids:
                                    for prod in data:
                                        if prod['user_id'] == user_id:
                                            print("\n".join(f"{key}: {value}" for key, value in prod.items()))
                                else:
                                    print("You do not have product listings yet!")
                            elif choice == 2:
                                data = load_user_detail(1)
                                ids = [user['ID'] for user in data]
                                if user_id in ids:
                                    print(view_profile(farmer_json, user_id))
                                else:
                                    pass
                            elif choice == 3:
                                while True:
                                    print("1. Crops\n2. Livestock \n3. Back")
                                    prod_cat_selection = int(input("Select from the categories above: "))
                                    if prod_cat_selection == 1:
                                        product_form(farmer_details, 'crops')
                                    elif prod_cat_selection == 2:
                                        product_form(farmer_details, 'livestock')
                                    elif prod_cat_selection == 3:
                                        break
                                    else:
                                        print("Invalid choice! Try again")
                            else:
                                print("Invalid choice! Try again")
                    elif choice_sel == 2:
                        user_detail = user_form()
                        if user_detail:
                            print("1. Crops\n2. Livestock\n3. Back")
                            prod_cat_selection = int(input("Select from the categories above: "))
                            if prod_cat_selection == 1:
                                farmer_selection(user_detail, 'crops')
                            elif prod_cat_selection == 2:
                                farmer_selection(user_detail, 'livestock')
                            elif prod_cat_selection == 3:
                                continue
                            else:
                                print("Invalid choice! Try again")
                        else:
                            pass
                    elif choice_sel == 3:
                        break
                    else:
                        print("Invalid choice! Try again")
            elif choice == 2:
                while True:
                    print(option_selection())
                    choice_sel = int(input('Please make your choice: '))
                    if choice_sel == 1:
                        while True:
                            user_id = input("Please enter your ID or press 0 to go back to previous menu: ")
                            folder = Path.cwd()
                            trader_json = folder / 'traders.json'
                            with open(trader_json, "r", encoding="utf-8") as f:
                                trader_details = json.load(f)
                                id_list = [trader_info["ID"] for trader_info in trader_details]
                            if user_id == '0':
                                break
                            if user_id not in id_list:
                                print(f"Invalid ID '{user_id}'! Please check again or Register as a new user.")
                            else:
                                while True:
                                    print('Welcome Registered Trader')
                                    print('What would you like to do? \n1. View Profile.\n2. Update Profile\n3. Make your order.\n4. Back')
                                    
                                    choice = int(input("Select from the option above: "))
                                    if choice == 1:
                                        print(view_profile(trader_json, user_id))
                                        print("=" * 20)
                                        print("Back to Previous Menu....")
                                    elif choice == 2:
                                        update_profile(trader_json, user_id)
                                        print("=" * 20)
                                        print('Profile updated successfully')
                                        print("Back to Previous Menu....")
                                    elif choice == 3:
                                        path = folder / 'products.json'
                                        name = input('Enter product ')
                                        order_products(path, name)
                                        # data = load_product()
                                        # user_data = load_user_detail(1)
                                        # for prod in data:
                                        #     print(prod)
                                        # data = load_product()
                                        # user_data = load_user_detail(1)
                                        # for prod in data:
                                        #     print(prod)
                                        # while True:
                                        #     prod_buy = int(input("Would you like to buy a product? 1 for yes and 2 for no: "))
                                        #     if prod_buy == 1:
                                        #         p_choice = input("Enter product ID")
                                        #         p_ids = [prod['ID'] for prod in data]
                                        #         if p_choice in p_ids:
                                        #             for prod in data:
                                        #                 if prod['ID'] == p_choice:
                                        #                     print("Contact Seller:")
                                        #                     for data in user_data:
                                        #                         if data["ID"] == prod["user_id"]:
                                        #                             print("Name: ", data['name'])
                                        #                             print("Location: ", data['location'])
                                        #                             print("Phone number: ", data['phone number'])
                                        #                             break
                                        #         else:
                                        #             print("Enter valid product ID please")
                                        #     elif prod_buy == 2:
                                        #         break
                                    elif choice == 4:
                                        break
                                
                    elif choice_sel == 2:
                        print(option_selection())
                        user_detail = user_form()
                        if user_detail:
                            user_detail = Users(user_detail.name, user_detail.age, user_detail.gender, user_detail.location, user_detail.phone_number)
                            buyer_details = buyer(user_detail.user_id, user_detail.name, user_detail.age, user_detail.gender, user_detail.location, user_detail.phone_number)
                            buyer_details.save_info()
                            print("Registration successful!!")
                        else:
                            print("Error completing registration.. :thinking_face:")
                    elif choice_sel == 3:
                        break
                    else:
                        print("Invalid choice! Try again")
            elif  choice == 3:
                print("Thank you for using AGROUSSD!")
                break
        except ValueError as e:
            print('Error:', e)
        # except Exception as e:
        #     print('Error:', e)
user_product()