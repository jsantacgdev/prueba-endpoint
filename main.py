from flask import Flask, jsonify, request

app = Flask(__name__)

### Función para combinar los datos de ventas y stock por Id de producto
def combine_data(product_sales, product_stock):
    # Crear diccionarios intermedios para las ventas y el stock
    sales_dict = {item["productId"]: item["sales"] for item in product_sales}
    stock_dict = {item["productId"]: item["stock"] for item in product_stock}

    # Combinar ambos en una lista final
    combined_data = []
    for product_id in sales_dict:
        combined_data.append({
            "productId": product_id,
            "sales": sales_dict[product_id],
            "stock": stock_dict[product_id]
        })

    return combined_data

@app.route('/sort-products', methods=['POST'])
def sort_products():
    unordered_list = request.get_json()
    ### Desglosamos el JSON de entrada.
    product_sales = unordered_list['productSales']
    product_stock = unordered_list['productStock']
    sales_weight = unordered_list['salesWeight']
    stock_weight = unordered_list['stockWeight']

    combined_data = combine_data(product_sales, product_stock)

    sorted_data = sorted(
        combined_data,
        key=lambda x: (x["sales"] * sales_weight) + (x["stock"] * stock_weight),
        reverse=True  # Orden descendente
    )

    ### Devolvemos el JSON ordenado.
    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run(debug=True)

