from flask import Flask, request, jsonify, abort
from models import ProductModel
product = ProductModel()

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/products', methods=['GET'])
def listarProdutos():
    product_name = request.args.get('product_name')
    expiration_date = request.args.get('date')

    if product.statusCode != 200:
        abort(400, 'Erro ao cadastrar o produto')

    return jsonify({
        "msg": 'Produto cadastrado com sucesso',
        "nome": product_name,
        'data_validade': expiration_date
    })
