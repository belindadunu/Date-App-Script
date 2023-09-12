# Create a date.py script that is a date simulator and does the following:

import time
import locale # Based on https://docs.python.org/3/library/locale.html
locale.setlocale(locale.LC_ALL, 'en_US.utf8') # Set locale to en_US to enable currency formatting in U.S. currency ($)

############################################# Define functions #############################################

# Prompts user to press enter continue
def press_enter_continue():
    while True:
        user_input = input("Press Enter to continue or 'q' to quit... ")
        if user_input == '':
            print("Great! Lets get started!")
            break # exit loop 
        elif user_input == "q":
            print("Goodbye!")
            quit()
        else:
            print("Please press Enter to continue.")

# Menu dictionary with keys as item ids
def print_menu(menu, category):
  print(category)
  # id represents the key for each menu item
  for id, item in menu[category].items():  
    # Print name, price and description
    print(f"{id}. {item['name']} - {item['price']}")
    # id will be "1", then "2" etc.
    print(f"\t{item['description']}")

# Take order   
def take_order(menu, budget):
  order = []
  
  while True:
    category = input("What would you both like to order (drinks/appetizers/entrees/desserts), or 'done' to finish ordering: ")
    if category == "done":
      break

    if category in menu:
      print_menu(menu, category)
    else:
      print("Invalid category. Please choose from drinks, appetizers,entrees, or desserts.")
      continue
    
    # Take item order
    # id will be the key entered by user 
    item_ids_input = input("Enter item numbers separated by spaces (or 'done' to finish ordering): ")  
    if item_ids_input == "done":
      break

    item_ids = [int(id) for id in item_ids_input.split() if id.isdigit()] # Split input into a list of choices
    
    # Get menu item using id key
  
    for item_id in item_ids:
      if item_id in menu[category]:
        item = menu[category][int(item_id)]
        if item ["price"] <= budget:
          order.append(item)
          budget -= item['price']
          print(f"Ordered {item['name']} for {item['price']}")
          print(f"\t{item['description']}") # Escape sequence: used for creating indentation in the printed output
          print(f"Budget left: {locale.currency(budget, grouping=True)}")
        else:
          print(f"Can't afford item, budget left: {locale.currency(budget, grouping=True)}")
      else:
        print("Invalid choice")
  print(f"Budget left after ordering: {locale.currency(budget, grouping=True)}")

  # Prompt the user to confirm paying the bill
  confirm_payment = input("Do you agree to pay the bill? (yes/no): ").strip().lower()
  if confirm_payment == "yes":
      final_budget = budget
  else:
      print("You did not confirm payment. You're going to jail!")
      final_budget = 0

  return order, final_budget

# Determine second date
def check_second_date(budget):
    if budget < 25:
        return "You made it to the end of the date with very little left in your wallet. It might be tough to secure a second date, but sometimes it's just better to stay at home and work on yourself. Better luck next time!"
    elif budget >= 100:
        return "You know how to wine and dine while saving money? Impressive! Second date secured!"
    else:
        return "You have some budget left, so there's a chance for a second date."

############################################# Define menu #############################################
menu = {
    "drinks": {
        1: {"name": "sexy fish", "price": 25, "description": "espolon blanco tequila, aperol, elderflower, pomegranate, blood orange, sea mist"},
        2: {"name": "positano heat", "price": 21, "description": "joven mezcal, tangerine, calíbrese chili, cinnamon, lime, salt"},
        3: {"name": "true love's kiss", "price": 14, "description": "tangerine, lemon, white peach, ginger beer"},
        4: {"name": "water", "price": 0, "description": "still water"}
    },
    "appetizers": {
        5: {"name": "housemade, hand-Rolled savory croissant", "price": 9, "description": "sarawak peppercorns, cultured butter, fiore di sale"},
        6: {"name": "caprese salad", "price": 9, "description": "fresh tomatoes, mozzarella cheese, basil, and balsamic glaze"},
        7: {"name": "spinach and artichoke dip", "price": 8, "description": "creamy dip with spinach, artichokes, and melted cheese, served with tortilla chips"},
        8: {"name": "bruschetta", "price": 7, "description": "toasted baguette slices topped with fresh tomatoes, garlic, basil, and olive oil"}
    },
    "entrees": {
        9: {"name": "scallop al tartufo", "price": 38, "description": "live sea scallop, ginger-leek-vanilla dressing, hazelnut, summer truffle"},
        10: {"name": "wild new zealand langoustine", "price": 28, "description": "served with salsa verde, salsa pizzaiolo & lemon."},
        11: {"name": "pappardelle", "price": 38, "description": "berkshire pork sausage & sungold tomato ragu"},
        12: {"name": "fiola mare lobster ravioli", "price": 75, "description": "ginger, chives"}
    },
    "desserts": {
        13: {"name": "venetian tiramisu", "price": 18, "description": "coffee-soaked chocolate sponge, mascarpone zabaglione, warm coffee foam, chocolate sorbetto"},
        14:{"name": "gelato", "price": 18, "description": "3 scoops"},
        15: {"name": "sorrento lemon", "price": 20, "description": "prosecco sgroppino, limoncello soaked almond cake, crystalized basil, amalfi style"},
        16: {"name": "bomboloni", "price": 20, "description": "ricotta donuts, chai tea budino, fior di latte froth, spiced sugar"}
    }
}

############################################# Start of prompt #############################################
print("Welcome to the Love Calculator - your budget-conscious cupid!\nLet's calculate if your budget matches your dreams of a second date.")

press_enter_continue()

# Vars
dates_name = input("Who are you going on a date with today? ")
restaurant_name = "Fiola Mare"
restaurant_rating = "$$$$"


print(f"Okay, great! I see you chose to take {dates_name.capitalize()} to {restaurant_name} -- an excellent choice.")

budget = int(input("What's your budget for today? "))

print(f"{restaurant_name} is rated {restaurant_rating}, so let's see what {locale.currency(budget, grouping=True)} can get you and your date here.")
time.sleep(2)

print(f"Currently, you have spent $0 of your {locale.currency(budget, grouping=True)}")
time.sleep(2)

# Call the print_menu functiom
print_menu(menu, "drinks")
time.sleep(3)
print_menu(menu, "appetizers")
time.sleep(3)
print_menu(menu, "entrees")
time.sleep(3)
print_menu(menu, "desserts")
time.sleep(3)

# Take orders
order, final_budget = take_order(menu, budget)
print(f"Final budget: {locale.currency(final_budget)}")

# Check for second date
second_date_result = check_second_date(final_budget)
print(second_date_result)