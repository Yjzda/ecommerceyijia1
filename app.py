from flask import Flask,request, jsonify
from model import customer_purchased_item
import persistance
app = Flask(__name__)

@app.route("/item-purchase",method='POST')
def purchase_item():
    product_name=request.json['product_name']
    quantity=request.json['quantity']
    inventory=persistance.find_inventory()
    customer_purchased_item(product_name,quantity,inventory,persistance)
    persistance.save_inventory()
    return jsonify({"message":"product ajouté au panier"})