#achat/commerce/logistique
#première chose: renommer les fonctions d'un code des autres

def get():
    #couche persistance
    inventory = {"apple": 50, "banana": 25, "orange": 33}
    return inventory


def is_product_quantity_enough(item_id:int, quantity:int, inventory_db:str)->int and int:
    #c'est couche métier mais pas un use case
    """
    check a given product exists with enough item. 
    
    """
    return item_id in inventory_db.keys() and inventory_db[item_id] >= quantity


def customer_purchase_item(item_id:int, quantity:int, inventory_db:str) -> str:
    #couche métier/persistance
    #c'est usecase et couche métier
    if item_id in inventory_db and inventory_db[item_id] >= quantity:
        inventory_db[item_id] -= quantity  # Shipped
 
        
    
def customer_purchase_multi_items(order_list:list, inventory_db:str):
    #couche métier/persistance
    for item_id, quantity in order_list:
        if item_id in inventory_db.keys() and inventory_db[item_id] >= quantity:
            #should be >=
            inventory_db[item_id] -= quantity
    #missing re
            

def generate_inventory_report(inv:str)->str:
    #couche interface
    report = "Stock Report:\n"
    for k, v in inv.items():
        report += f"Item ID: {k}, Quantity: {v}\n"
    return report

#achat/commerce/logistique
#première chose: renommer les fonctions d'un code des autres

def get():
    #couche persistance
    inventory = {"apple": 50, "banana": 25, "orange": 33}
    return inventory


def is_product_quantity_enough(item_id:int, quantity:int, inventory_db:str)->int and int:
    #couche persistance/métier
    """
    check a given product exists with enough item. 
    
    """
    return item_id in inventory_db.keys() and inventory_db[item_id] >= quantity


def customer_purchase_item(item_id:int, quantity:int, inventory_db:str) -> str:
    #couche métier/persistance
    if item_id in inventory_db and inventory_db[item_id] >= quantity:
        inventory_db[item_id] -= quantity  # Shipped
 
        
    
def customer_purchase_multi_items(order_list:list, inventory_db:str):
    #couche métier/persistance
    for item_id, quantity in order_list:
        if item_id in inventory_db.keys() and inventory_db[item_id] >= quantity:
            #should be >=
            inventory_db[item_id] -= quantity
    #missing re
            

def generate_inventory_report(inv:str)->str:
    #couche interface
    report = "Stock Report:\n"
    for k, v in inv.items():
        report += f"Item ID: {k}, Quantity: {v}\n"
    return report

