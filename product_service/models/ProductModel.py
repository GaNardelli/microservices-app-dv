class ProductModel:
    def __init__(self):
        self.nome = ''
        self.data_validade = ''
        pass

    def insert_product(self, nome, data_validade):
        self.nome = nome
        self.data_validade = data_validade
        return ({'statusCode': 200, 'msg': 'produto cadastrado'})
