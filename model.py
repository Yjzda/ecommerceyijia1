from typing import Dict
#from fake_persistance import save_inventory
import fake_persistance
#inventory = {"apple": 50, "banana": 25, "orange": 33}

def is_product_quantity_enough(product_name:str, quantity:int, inventory_db:Dict[str,int])->int and int:
    #couche persistance/métier
    """
    check a given product exists with enough item. 
    
    """
    return product_name in inventory_db.keys() and inventory_db[product_name] >= quantity

#use case: événement métier
def customer_purchased_item(product_name:int, quantity:int, inventory_db:str,fake_persistance) -> str:
    #couche métier/fake_persistance
   # if product_name in inventory_db and inventory_db[product_name] >= quantity:
   if is_product_quantity_enough(product_name,quantity,inventory_db):
        inventory_db[product_name] -= quantity  # Shipped
    #fake_persistance: injection dépendance on donne un faux argument
        fake_persistance.save_inventory(inventory_db)
    
def customer_purchase_multi_items(order_list:list, inventory_db:dict,fake_persistance):
    #couche métier/fake_persistance
    for order in order_list:
        for product_name, quantity in order.items():
       # if product_name in inventory_db.keys() and inventory_db[product_name] >= quantity:
            if is_product_quantity_enough(product_name,quantity,inventory_db):
                customer_purchased_item(product_name,quantity,inventory_db,fake_persistance)
  



