from persistance import find_inventory, add_product, update_quantity, save_inventory
import fake_model

def test_find_inventory():
    inventory = find_inventory()
    assert isinstance(inventory, dict)
    assert inventory.get("apple") == 50
    assert inventory.get("banana") == 25
    assert inventory.get("orange") == 33

def test_add_product():
    add_product("grape", 10)
    inventory = find_inventory()
    assert inventory.get("grape") == 10

def test_update_quantity():
    update_quantity("apple", 60)
    inventory = find_inventory()
    assert inventory.get("apple") == 60

def test_save_inventory():
    new_inventory = {"apple": 60, "banana": 30, "orange": 40}
    save_inventory(new_inventory)
    inventory = find_inventory()
    assert inventory.get("apple") == 60
    assert inventory.get("banana") == 30
    assert inventory.get("orange") == 40
