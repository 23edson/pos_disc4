import os
from fastapi import FastAPI, Request
import json
from datetime import datetime
import uvicorn


app = FastAPI(
    title="Trabalho 2 - Desenvolvimento Back-end",
    description="Mais detalhes da documentação no arquivo - README.md",
    openapi_tags=[ {
        "name": "send_file",
        "description": "Endpoint responsável por receber um JSON e salvar o resultado em arquivo no servidor.",
    },
    {
        "name": "next_file",
        "description": "Retorna o próximo arquivo na fila a ser processado",
    },]
)


#Estado inicial de controle
initial_state = {
    'next': '',
    'list': [],
    'processed' : []
}

database = 'ctrlfile.json'

# Essa função é responsável por salvar os dados de controle
def set_control_data(new_data):

    try:
            
        with open(database, 'w+') as db:
            json.dump(new_data, db, indent=4)
    except ValueError as serverDebug:
        print('erro ao salvar dados de controle', serverDebug)
        return False


# Essa função busca os dados salvos no arquivo de controle
def get_control_data():

    try:
        with open(database, 'r') as db:
            data = json.load(db)
        
    except FileNotFoundError as ve :
        with open(database, 'w+') as db:
            json.dump(initial_state, db, indent=4)
            data = initial_state
    return data


@app.post('/send_file', tags=['send_file'])
async def save_data(data_to_save : Request):

    """
        Esse endpoint é responsável por criar um arquivo json conforme a requisição submetida

    """

    try:
        #json da request
        json_data = await data_to_save.json()
    except:
        return {'message': 'Erro ao processar os dados da requisição!'}
    
    #cria um novo arquivo com a data atual
    new_filename = str(datetime.today().strftime('%Y_%m_%d_%H_%M_%S')) + '.json'

    #busca os dados de controle
    ctrl_data = get_control_data()
   
    #adiciona o novo arquivo na lista de arquivos
    new_list = ctrl_data['list']
    new_list.append(new_filename)

    #ordena a lista de arquivos para facilitar a busca pelo próximo
    ctrl_data['list'] = sorted(new_list)

    #posição inicial da lista será o próximo
    ctrl_data['next'] = ctrl_data["list"][0]
  
    #atualiza o arquivo de controle
    set_control_data(ctrl_data)

    #cria diretório se não existir
    if not os.path.exists('files'):
        os.makedirs('files')
        
    #escreve no banco os dados atualizados
    with open('files/' + new_filename, 'w+') as f:
        json.dump(json_data, f, indent=4)

    return {'Dados salvos!'}

@app.get('/get_next_file', tags=["next_file"])
def get_next_data():

    """
        Esse endpoint é responsável por buscar o próximo arquivo da fila e devolver o 
        resultado ao usuário. Caso a fila esteja vazia, apenas avisa.
    
    """

    #busca os dados de controle
    ctrl_data = get_control_data()

    #se não há próxima, apenas avisa o usuário
    if ctrl_data['next'] == '':
        return {'message': 'Sem arquivos na fila!'}
    
    next_file = ctrl_data['next']

    try:
        #carrega o próximo arquivo da lista
        with open('files/' + next_file, 'r') as f:
            data = json.load(f)
           
            #remove o primeiro arquivo da lista de controle (próximo)
            ctrl_data['list'] = ctrl_data['list'][1:]
            #define se há um próximo
            ctrl_data['next'] = "" if len(ctrl_data['list']) == 0 else ctrl_data['list'][0]
            #adiciona o arquivo na lista de processados
            ctrl_data['processed'].append(next_file)

            #atualiza o arquivo de controle
            set_control_data(ctrl_data)

            return { 'filename': next_file, 'data' : data }
        
    except FileNotFoundError as serverDebug:
        print("Problema ao processar os arquivos!", serverDebug)
        return {'message': 'Problema ao processar os arquivos!'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)