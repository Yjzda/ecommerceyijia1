inventory = {"apple": 50, "banana": 25, "orange": 33}
def find_inventory_by_id():
    #couche persistance
   
    return inventory
def add_product(name:str,quantity:int):
    inventory[name]=quantity

def update_quantity(product_name,quantity):
    inventory[product_name]=quantity
def save_inventory(new_inventory):
    inventory=new_inventory
