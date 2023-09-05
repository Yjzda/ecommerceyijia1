# Initialize the inventory dictionary
inventory = {"apple": 50, "banana": 25, "orange": 33}

# Find and return the inventory
def find_inventory(fake_model=None):
    return inventory

# Add a product to the inventory
def add_product(name: str, quantity: int, fake_model=None):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

# Update the quantity of a product in the inventory
def update_quantity(product_name, quantity, fake_model=None):
    if product_name in inventory:
        inventory[product_name] = quantity
    else:
        raise ValueError(f"Product '{product_name}' not found in inventory.")

# Save the inventory with a new dictionary
def save_inventory(new_inventory, fake_model=None):
    global inventory
    inventory = new_inventory
