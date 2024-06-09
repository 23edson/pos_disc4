from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI()

initial_state = {
    'next': '',
    'list': [],
    'processed' : []
}

database = 'ctrlfile.json'

def set_control_data(new_data):

    try:
        with open(database, 'w+') as db:
            json.dump(new_data, db, indent=4)
    except ValueError as ve:
        print('erro ao salvar dados de controle')
        return False


def get_control_data():

    try:
        with open(database, 'r') as db:
            data = json.load(db)
        
    except FileNotFoundError as ve :
        with open(database, 'w+') as db:
            json.dump(initial_state, db, indent=4)
            data = initial_state
    return data, db

# Essa função é responsável por criar um arquivo json conforme a requisição submetida
@app.post('/send_file')
async def save_data(data_to_save : Request):

    json_data = await data_to_save.json()
    
    next_filename = str(datetime.today().strftime('%Y_%m_%d_%H_%M_%S')) + '.json'

    ctrl_data = get_control_data()
   
    new_list = list(ctrl_data["list"])
    new_list.append(next_filename)
  
    ctrl_data["list"] = new_list
  
    set_control_data(ctrl_data)

     #escreve no banco os dados atualizados
    with open('files/' + next_filename, 'w+') as f:
        json.dump(json_data, f, indent=4)

    return {'Dados salvos!'}

# Essa função é responsável por retornar o valor total computado de um client
@app.get('/get_next_file')
def get_next_data():
    return {'ok'}