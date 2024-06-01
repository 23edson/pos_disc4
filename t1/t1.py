from fastapi import FastAPI
from pydantic import BaseModel
import json

#Representa um produto
class Product(BaseModel):
    name: str
    qtd: int
    price: float

app = FastAPI()

database = 'filedb.json'

# Função para buscar um client no banco de dados da aplicação
def find_dbclient(client_id):

    with open(database, 'r') as db:
        try:
            data = json.load(db)
        
        except ValueError as ve :
            data = []

        #procura no vetor json o client requisitado
        for idx, json_item in enumerate(data):
            if json_item['client_id'] == client_id:
                return idx, json_item, data
    return -1, None, data


# A função recebe a quantidade e o preço de um produto e retorna a o valor multiplicado 
def sum_price(qtd, price):
    return price * qtd

# Essa função é responsável por adicionar o valor de um produto ao somatório armazenado na aplicação
@app.post('/set-product/{client_id}')
def set_product(client_id, product: Product):

    item_indx, item, data = find_dbclient(client_id)

    #se estiver vazio, apenas acrescenta            
    if item_indx == -1:
        data.append({
            'client_id': client_id,
            'total' : sum_price(product.qtd, product.price)
        })

    #se encontrou, soma o valor do produto ao total  
    else:
        item['total'] += sum_price(product.qtd, product.price)
        data[item_indx] = item

    #escreve no banco os dados atualizados
    with open('filedb.json', 'w+') as f:
        json.dump(data, f, indent=4)

    return {'Product computed!'}

# Essa função é responsável por retornar o valor total computado de um client
@app.get('/get-total/{client_id}')
def get_total(client_id):

    item_indx, item, Null = find_dbclient(client_id)

    if(item_indx == -1):
        return {'Client not found!'}

    return {'Total': item['total']}