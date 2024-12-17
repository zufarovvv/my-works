from project.database import load_data


def add_form(products):
    name = input(" Enter your company name: ")
    product = input(" Enter product name: ")
    location = input(" Enter location: ")
    products.append({'name': name, 'product': product, 'location': location})

    data = load_data()
    data.append(products)

    while True:
        try:
            choice = input("Do you want to add another product? (Yes|No): ").strip().lower()
            if choice == 'yes':
                return add_form(products)
            elif choice == 'no':
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid input: "Yes" or "No".')


def print_product(products):
    if not products:
        print("No products entered")
    else:
        for product in products:
            print(f' Company Name: "{product["name"]}" Product Name: "{product["product"]}" Product Location: "{product["location"]}"\n')


def sign_up_form(users):
    for user in users:
        if user in users:
            main()
        else:
            print("You are not found. Please Sign up ")
            check_users(users)


def check_users(users):
    while True:
        try:
            username = input("Enter your username: ").strip().lower()
            password = input("Enter your password: ").strip().lower()
            users.append({'username': username, 'password': password})
            if len(username) < 5:
                print("Username is too short")
                break
            elif len(password) > 3:
                print("Password accepted!\n")
                main()
            else:
                raise Exception("Password is too short")
        except Exception as e:
            print(e)


def search_products(product):
    med = input("Enter product name: ")

    if med in product:
        print(f' Company Name: "{product["name"]}" Product Name: "{product["product"]}" Product Location: "{product["location"]}"\n')
    else:
        print(f"'{med}' not found")
        while True:
                try:
                    choice = input("Search another product? (Yes|No): ")

                    if choice == 'yes':
                        return search_products(product)
                    elif choice == 'no':
                        break
                    else:
                        raise Exception
                except Exception:
                    print('Please enter a valid input: "Yes" or "No".')


def about_us():
    info = '''
ABOUT US!
"FOM Group"
Web Site: https://fomgroup.uz/
Telegram: https://t.me/fomgroupsupport
You Tube: https://www.youtube.com/@FOMGroup
     '''
    print(info)


def registration():
    products = []
    users = []

    while True:
        print('1. The pharmacist')
        print('2. The customer')
        print('3. About Us')
        try:
            choice = input('Enter your choice: ')
            # Pharmacist view
            if choice == '1':
                check_users(users)
            elif choice == '2':
                search_products(products)
            elif choice == '3':
                about_us()
            else:
                raise Exception("Error")
        except Exception as e:
            print(e)


def main():

    products = []

    while True:
        print(" Welocme!")
        print('1. Add Product ')
        print('2. Products List ')
        print('3. Quit')

        choice = input(" Enter your choice: ")

        if choice == '1':
            add_form(products)
        elif choice == '2':
            print(" All Products\n")
            print_product(products)
        elif choice == '3':
            print(" Good Bye!")
            exit()
        else:
            print("Invalid chice. Please enter 1, 2, 3: ")


registration()



