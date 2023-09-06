def generate_stock_report(inv):

    report = "Stock Report:\n"
    for k, v in inv.items():
        report += f"product_name: {k}, Quantity: {v}\n"
    return report
