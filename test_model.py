from model import customer_purchased_item
import fake_persistance
def test_custom_purchased_item():
    inventory={
        'apple':10,
        'pear':5
    }
    #scénario 1
    product_name="apple"
    quantity=5
    error=customer_purchased_item(product_name,quantity,inventory,fake_persistance)
    fake_persistance.save_inventory(inventory)
    #injection dépendance
    
    #si la fonction marche alors inventory.. =5
    assert inventory['apple']==5
    assert error is None

    #scénario 2
    
    product_name="poulet"
    quantity=5
    error=customer_purchased_item(product_name,quantity,inventory,fake_persistance)
    fake_persistance.save_inventory(inventory)
    assert inventory['poulet']==5
    assert error is not None
    

