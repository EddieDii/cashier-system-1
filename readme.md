There are 3 parts; please ensure you only attempt one part after completing the previous part.
# Part 1
In this part, your program can perform some simple interactions with users (i.e., the pharmacists):
1. Display a message asking the user to enter the customer’s name. In this part, you can assume the customer name to be entered only consists of alphabet characters.
2. Display a message asking the user to enter the name of the product the customer chooses. In this part, you can assume the product to be entered is always a valid product.
3. Display a message asking the quantity of the product ordered by the customer that was entered earlier. In this part, you can assume the quantity to be entered is always a positive integer, e.g.,1, 2, 3 …
4. Calculate the total cost for the customer. The total cost is equal to the product’s unit price multiplying with the product quantity. For example, if the product is vitaminC, the unit price of this product is 12$, and if the product quantity is 3, then the total cost is 36$.
5. Calculate the reward points earned by the purchase. For each 1$, there will be 1 reward point. The reward points will be rounded. For example, if the purchase is 35.5$, the corresponding reward point is 36. If the purchase is 35.4$, the corresponding reward point is 35.
6. All the purchase information will be displayed as a formatted message to the user as follows. Note that the product’s unit price and total cost are all displayed with two digits after the decimal point.
7. In the program, you should have some lists (or dictionaries or other data types) to store the names of all customers, the accumulated reward points of the customers, the available products, the unit prices of the products. You can assume the customer names and the product names are all unique and case sensitive.
8. When a new customer finishes a purchase, your program will automatically add the customer's name to the customer list and the earned reward points to the customer profile. When an existing customer finishes a purchase, your program will add the earned reward points to the customer profile.
9. Your program needs to be initialized with the following existing customers: Kate and Tom, with the reward points being 20 and 32 respectively. Your program will also be initialized with the following products: vitaminC, vitaminE, coldTablet, vaccine, and fragrance with the corresponding prices: 12.0, 14.5, 6.4, 32.6, and 25.0.
10. Note: in the requirements No. 7, we use the term 'list' when describing the customer list, the product list, etc, but you can use other data types to store this information such as dictionaries and other data types. Make sure you think and analyse the requirements in detail so that you can choose the most appropriate/suitable data types.