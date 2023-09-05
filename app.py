from flask import Flask,request, jsonify
from model import customer_purchased_item
import persistance
app = Flask(__name__)

@app.route("/item-purchase",methods=['POST'])
def purchase_item():
    product_name=request.json['product_name']
    quantity=request.json['quantity']
    inventory=persistance.find_inventory()
    customer_purchased_item(product_name,quantity,inventory,persistance)
    persistance.save_inventory(inventory)
    return jsonify({"message":"product ajouté au panier"})

@app.route("/get-info", methods=['GET'])
def get_info():
    return jsonify({"message": "This is a GET endpoint for retrieving information."})

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable favicon caching
    app.run(debug=True)