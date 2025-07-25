# Dictionary of items with codes, names, and prices
# This is the menu for the vending machine
items = {
    # Drinks section
    "A1": {"name": "Coca-Cola", "price": 1.5},
    "A2": {"name": "Pepsi", "price": 1.4},
    "A3": {"name": "Karak Chai", "price": 1.5},
    "A4": {"name": "Rani Float", "price": 1.5},;

    # Chips and crispy snacks
    "B1": {"name": "Lays Chips", "price": 1.2},
    "B2": {"name": "Oman Chips", "price": 1.1},         
    "B3": {"name": "Pringles Mini", "price": 1.6},
    "B4": {"name": "Cheetos", "price": 1.3},

    # Chocolate items
    "C1": {"name": "Galaxy Chocolate Bar", "price": 1.0},
    "C2": {"name": "KitKat", "price": 1.0},
    "C3": {"name": "Snickers", "price": 1.2},
    "C4": {"name": "Kinder Bueno", "price": 1.4},

    # Sweet snacks like cakes and biscuits
    "D1": {"name": "Lulu Cake Roll", "price": 1.2},      
    "D2": {"name": "Baladi Kunafa Bar", "price": 1.5},   
    "D3": {"name": "Cream-Filled Croissant", "price": 1.3},
    "D4": {"name": "Digestive Biscuit Pack", "price": 1.0},

    # Savory and local snacks
    "E1": {"name": "Cheese Sambosa Pack", "price": 1.8}, 
    "E2": {"name": "Mini Shawarma Wrap", "price": 2.5},  
    "E3": {"name": "Spicy Popcorn Tub", "price": 1.6},
    "E4": {"name": "Mini Pizza Slice", "price": 2.0}
}

# Function to show the menu to the user
def display_menu():
    print("Welcome to the Vending Machine!\n")
    print("Here are the available items:\n")
    print("{:<5} {:<20} {:<5}".format("Code", "Item", "Price (Dhs)"))  # Table headers
    print("-" * 35)
    for code, item in items.items():
        # Print each item in a nice format
        print("{:<5} {:<20} {:<5}".format(code, item['name'], item['price']))
    print()  # Extra line for spacing

# Function to get the item the user wants
def get_item_choice():
    code = input("Enter the item code you want to purchase: ").upper()  # Ask for item code
    if code in items:  # If code is valid
        return code
    else:
        print("Invalid code. Please try again.\n")  # Error message
        return get_item_choice()  # Ask again

# Function to take money and calculate change
def process_payment(price):
    print(f"The item costs Dhs{price:.2f}")  # Show price
    money = float(input("Insert money (Dhs): "))  # Take user’s money
    if money < price:
        print("Insufficient funds. Please insert more money.")  # Not enough money
        return process_payment(price)  # Ask again
    change = round(money - price, 2)  # Calculate and round change
    return change

# Main function to run the vending machine
def vending_machine():
    display_menu()  # Show items
    code = get_item_choice()  # Ask user what they want
    selected_item = items[code]  # Get item info
    change = process_payment(selected_item['price'])  # Handle payment

    # Final messages
    print(f"\nDispensing {selected_item['name']}...")  # Show item being given
    print(f"Here is your change: Dhs{change:.2f}")  # Show change
    print("Thank you for using the vending machine!")  # Goodbye message

# Start the vending machine
vending_machine()
