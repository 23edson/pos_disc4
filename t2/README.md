## Trabalho 1 / Desenvolvimento Back-end / Pós-Graduação

-Edson Lemes da Silva   

A aplicação tem uma simples função: 
Recebe o nome, quantidade e valor de um ou mais produtos
e ao final devolve o somatório do valor ao usuário. 

Desenvolvido com a versão do python: 3.11.2 

Existem duas implementações nesse projeto:

1. Aplicação via prompt de comando
2. Aplicação em formato API

## 1. Aplicação via prompt de comando
Para executar a aplicação via prompt de comando, basta executar o comando: `python3 t1-prompt.py`

O programa irá pedir o nome do produto, a quantidade e o valor do produto. Em seguida irá 
solicitar se o usuário deseja incluir mais produtos (sim ou não). No momento que o usuário
responder não, o programa irá devolver o somatório dos valores dos produtos.

## 2. Aplicação via API

Para executar a aplicação, é necessário ter os pacotes baixados via pip, para isso pode ser utilizado o comando: `pip install -r requirements.txt`.

 Após isso, o seguinte comando para iniciar a aplicação: `python3 -m uvicorn t1:app`.

Essa segunda versão utiliza o FastAPI como dependência. Para representar o armazenamento em um banco de dados, foi criado de forma simplificada um arquivo chamado `filedb.json`, este por sua vez guarda as informações submetidas através do endpoint de insert. Além disso, o mesmo arquivo é utilizado para as consultas.

Existem dois endpoints configurados:

1. `http://localhost:8000/set-product/{client_id}`: método: [POST],

     body exemplo: {
    "name" : "Tv",
    "qtd": 1,
    "price" : 2.5
}

    Esse método é responsável por computar o valor e a quantidade de um produto de acordo com o `client_id` passado por parâmetro. Exemplo de requisição: http://localhost:8000/set-product/5

2. `http://localhost:8000/get-total/{client_id}` : método: [GET]

    Esse método é responsável por retornar ao usuário o valor total armazenado no banco de dados. Exemplo de requisição: http://localhost:8000/get-total/5

## Dependências

* FastAPI para a segunda versão: `t1.py`
* Alguns pacotes base do python 
