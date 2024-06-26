# initialized info
customers = {
    "Kate" :{'points': 20, 'history': []},
    "Tom" : {'points': 32, 'history': []}
}
products = {
    "vitaminC": {'price': 12.0, 'prescription': False},
    "vitaminE": {'price': 14.5, 'prescription': False},
    "coldTablet": {'price': 6.4, 'prescription': False},
    "vaccine": {'price': 32.6, 'prescription': True},
    "fragrance":{'price': 25.0, 'prescription': False}
}   

# make purchase function
def make_purchase():
    # enter customer name
    while True:   # creates an infinite loop, the program will continuously receive user inputs until the conditions are met.
        #Can have whitespaces before and after the input
        customer_name = input("Enter the name of the customer[e.g. Eddie]: ").strip()
        # Only contains alphabet  characters 
        if not customer_name.isalpha():
            print("Invalid name. Only alphabet characters are allowed.")
            continue
        elif customer_name not in customers:
            customers[customer_name] =  {'points': 0, 'history': []}
        break

    # enter product name
    while True: # outside loop, check input until valid input. 
        is_input_valid = True
        valid_products = []
        product_list = input("Enter the product name:[enter valid products only, e.g. vitaminC, coldTablet]: ").split(',')
        for single_product in product_list: # check input prodcuts are in the product list
            single_product = single_product.strip() # remove the whitespaces before and after the content
            if single_product not in products:
                is_input_valid = False
                print("The product is not valid. Please enter a valid product.")
                break
            else:
                valid_products.append(single_product)

        if not is_input_valid: # re-input
            continue

        while True: # inner loop, check quantities until vaild quantities
            is_input_valid = True
            valid_quantities = []
            quantity_list = input("Enter the quantities[enter positive integers only, e.g. 1, 2, 3, 4]: ").split(',')
            # count the input product number and the quantity number
            if len(product_list) != len(quantity_list):
                print("The number of products and quantities do not match.")
                continue
            # enter product quantity
            for q in quantity_list:
                try:
                    if int(q) <=0:
                        is_input_valid = False
                        print("Quantities must be positive integers.")
                        break
                    else:
                        valid_quantities.append(int(q))
                except ValueError:
                    is_input_valid = False
                    print("Invalid input. Please enter integers only.")
                    break
            if is_input_valid:
                break # break inner loop
        
        # check prescription
        needs_prescription = False
        for p in valid_products:
            if products[p]['prescription']:
                needs_prescription = True
                break
        if needs_prescription:
            while True:
                prescription = input("The product vaccine requires a doctor's prescription. Do you have one (y/n)? ").strip()
                if prescription.lower() == 'n':
                    print("The product vaccin cannot proceed without a prescription. Removing prescription items.")
                    # create temporary list to store the information of products
                    temp_products = []
                    temp_quantities = []
                    for p,q in zip(valid_products, valid_quantities):
                        # for products do not need prescription, store in the temporary list
                        if not products[p]['prescription']:
                            temp_products.append(p)
                            temp_quantities.append(q)
                    valid_products = temp_products
                    valid_quantities = temp_quantities
                    # after remove the product that need prescription, show this message if the list is empty.
                    if not valid_products:
                        print("No products left to purchase after removing prescription items.")
                        return
                    break

                elif prescription.lower() == 'y':
                    break
                else:
                    print("The answer is not valid. Please enter a valid an answer.")
                    continue

        # Calculate total cost and reward points
        if valid_products:
            total_cost = 0  # initialize total_cost
            # Multiply the price of an product by the quantity and add it to the total cost
            for p,q in zip(valid_products, valid_quantities):
                total_cost += products[p]["price"] * q
            # Compare the redeemable point with the total cost, customer cannot redeem more points than the total cost.
            redeemable_money = min(customers[customer_name]['points'] // 100 *10, total_cost)
            reward_points = round(total_cost)
            total_cost -= redeemable_money
            # new_points is the final reward_points that will update to the customer's infomation.
            new_points = customers[customer_name]['points'] + reward_points - redeemable_money * 10
            # update customer points and history
            customers[customer_name]["points"] = new_points
            customers[customer_name]["history"].append({
                "products": [(p, q) for p, q in zip(valid_products, valid_quantities)],
                "total_cost": total_cost,
                "earned_rewards": reward_points
            })
        
        # receipt format
        def print_receipt(customer_name, valid_products, valid_quantities, total_cost, reward_points):
            print('-' * 45)
            print("Receipt".center(45, ' '))
            print('-' * 45)
            print(f'Name: \t\t\t{customer_name}')
            print('-' * 45)
            for name, qty in zip(valid_products, valid_quantities):
                print(f"Product: \t\t{name}")
                print(f"Unit Price: \t\t{products[name]['price']:.2f}(AUD)")
                print(f"Quantity: \t\t{qty}")
            print('-' * 45)
            print(f"Total cost: \t\t{total_cost:.2f}(AUD)")
            print(f"Earned reward: \t\t{reward_points}")
        print_receipt(customer_name, valid_products, valid_quantities, total_cost, reward_points)
        break # outside loop ends.
 
# Add/update information of a product function
def add_or_update_product():
    while True:
        product_info =input("Enter information of products[e.g. vitaminC 15 n, vitaminE 20 n): ").split(',')
        is_valid = True
        updated_products = {}
        for single_product in product_info:
            single_product_info = single_product.strip().split()
            name, price, prescription_required = single_product_info
            try:
                if float(price) <= 0 or prescription_required.lower() not in ['y', 'n']:
                    is_valid = False
                    break
                updated_products[name] = {'price': float(price), 'prescription': prescription_required.lower()=='y'}
            except ValueError:
                is_valid = False
                break
        if is_valid:
            products.update(updated_products)
            for name in updated_products:
                print(f"Product '{name}' has been added/updated successfully.")
            break
        else:
            print("Invalid input. Please enter the whole list again.")

# Display existing customers function
def display_customers():
    print('-' * 40)
    print("Existing Customers List".center(40, ' '))
    print('-' * 40)
    print('Customer Name'.ljust(25), 'Reward Points'.ljust(15))
    for customer, detail in customers.items():
        print(customer.ljust(25), str(detail['points']).ljust(15))

#Display existing products
def display_products():
    print('-' * 50)
    print("Products List".center(50, ' '))
    print('-' * 50)
    print('Product'.ljust(20), 'Price'.ljust(15), 'Prescription?'.ljust(15))
    for product, detail in products.items():
        # change the prescription showing format, from True/False to Yes/No
        if detail['prescription'] is True:
            prescription = 'Yes'
        else:
            prescription = 'No'

        print(product.ljust(20), str(detail['price']).ljust(15), prescription.ljust(15))

# Display a customer order history
def display_customer_order_history():
    while True:
        customer_name = input("Enter customer's name: ").strip()
        if customer_name not in customers:
            print("This customer does not exist.")
            continue
        # if history list is empty, print this message, and ends the function.
        if not customers[customer_name]["history"]:
            print(f"Sorry, {customer_name} has no order history.")
            break
        max_product_length = 0
        for order in customers[customer_name]["history"]:
            product_line = [f"{qty} x {prod}" for prod, qty in order["products"]]
            products_str = ", ".join(product_line)
            # through comparing the length of each order's product list to find the max length of product list, add 3 to get more space
            if len(products_str) > max_product_length:
                max_product_length = len(products_str) + 3

        print(f"This is the order history of {customer_name}.")
        print(f"{'     '.ljust(10)} {'Products'.ljust(max_product_length)} {'Total Cost'.rjust(15)} {'Earned Rewards'.rjust(15)}")
        for i, order in enumerate(customers[customer_name]["history"], start=1):
            product_line = [f"{qty} x {prod}" for prod, qty in order["products"]]
            products_str = ", ".join(product_line)
            print(f"Order {str(i).ljust(4)} {products_str.ljust(max_product_length)} {format(order['total_cost'], '.1f').rjust(15)} {str(order['earned_rewards']).rjust(15)}")
        
        break

#operated using a menu
def show_menu():
    while True:
        print('Welcome to the RMIT pharmacy!'.center(60))
        print("#"*60)
        print(f"""
            You can choose from the following options:
            1. Make a purchase
            2. Add/update information of a product
            3. Display existing customers
            4. Display existing products
            5. Display a customer order history
            6. Exit the program
            """)
        print("#"*60)
        option = input("Please choose an option: ").strip()
        print(f"You choose option {option}.")
        if option == '1':
            make_purchase()
        elif option == '2':
            add_or_update_product()
        elif option == '3':
            display_customers()
        elif option == '4':
            display_products()
        elif option == '5':
            display_customer_order_history()
        elif option == '6':
            print("Exit. Bye.")
            break
        else:
            print("Invalid option, please choose again.")

show_menu()
print(customers)


'''
Analysis/ Reflection:
After reaading the assignment spec, I first think of how I can store the 
data, dictionary is a good way. It's mre convenient to use a key rather
than an index in order to store and retrieve values.

I created 'make_purchase' method to implement the process of a user 
purchasing products, by using 'While True' infinite loop, the program 
will continuously receive user inputs until the conditions are met.
Then, I stored the input into the 'customers' dictionary one by one 
by using a 'for' loop. 
I used a similar nested loop approach to design the 'add_or_update_product' 
method and the 'display_customer_order_history' method. 
The 'display_customers' method was relatively easier to create, as it only required
a 'for' loop to print each customer's information form the existing customer dictionary. 
The 'display_products' method needed a 'for' loop nested with an 'if' statement
to convert the boolean type of 'prescription' into 'Yes' or 'No', which are easily 
for human to read. 
The 'show_menu' method required compiliing all the created methods into a printed list 
for the user to choose from. It also needed a 'while True' loop with additional
'if' statement to evaluate the user's input and execute the corresponding methods.

I have read offical python documents for several times, 
and through repeatedly studying and reading the documents on Canvas, 
combined with practice questions in practical sessions on Canvas,
I have undertood the approach to creating complex functions.

In my code, I have used numerous while True loops along with 
if condition statements and control statements (such as continue and break). 
This is a powerful method to ensure that user inputs meet the expected format 
and to easily handle errors or other invalid inputs.

The biggest challenge I encountered in Part 2 was using a while loop for outside loop, 
combine with nested while loop, if statements and for loops to validate inputs.
Becasue there were many loops with break and continue statements, 
my code texting often led to numerous errors.
Then I used https://pythontutor.com to help me understand the logic of 
nested loop relationships,
and to deeply understand the logic of break and continue statements.

In Part 3, a minor challenge was about how to split the input content.
When inputting multiple products connected by commas, I needed to first split the content
around the commas, then use a for loop to remove whitespaces from the beginning 
and end of each item, which took me a long time to figure out.

The biggest challenge in Part 3 was the 'display order history' section, because it 
required printing orders of varying lengths.
I made the product secion dynamiclly adjust based on the length of the longest 
product order, which involved addtional checks on the products list's length, 
it was the hardest part for me.

Addtionally, the feature added in Part 3 that allowed reward points to be converted to 
money and be deducted from the purchase also took a long time to correctly calculate 
the deduction from historical points, while ensuring that the current purchase reward points 
were updated and the deducted points were subtracted.
'''
