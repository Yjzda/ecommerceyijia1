from model import customer_purchased_item,customer_purchase_multi_items
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

def test_customer_purchased_multi_item():
    #scénario 1
    order_list=[{"apple":2,"banana":1},{"apple":1,'banana':1}]
    inventory={
        'apple':10,
        'pear':5,
        'banana':8
    }
    error=customer_purchase_multi_items(order_list,inventory,fake_persistance)
    fake_persistance.save_inventory(inventory)
    assert inventory['apple']==7
    assert inventory['banana'] == 6
    assert inventory['pear'] == 5

    assert error is None
    




