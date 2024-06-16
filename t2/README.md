## Trabalho 2 / Desenvolvimento Back-end / Pós-Graduação

-Edson Lemes da Silva   

A aplicação representa uma fila simples, onde existem dois 
endpoints: um que recebe dados em formato JSON e salva em arquivo no servidor; e um outro
que retorna os dados salvos em ordem sequencial, isto é, na ordem que estão dispostos na fila
de acordo com a data de inserção.

Os dados em JSON são armazenados na pasta `files`, o nome do arquivo representa o horário em que ele
foi submetido.

A aplicação cria um arquivo chamado `ctrlfile.json`, esse arquivo é utilizando para controle da fila. 
Nele existem três pontos de controle: next, list e processed
- `next`: Representa o próximo arquivo a ser lido.
- `list`: Representa a lista de arquivos criados (ordenados por data de criação).
- `processed`: Representa a lista de arquivos que já foram processados.

Desenvolvido com a versão do python: 3.11.2 


Para executar a aplicação, é necessário ter os pacotes baixados via pip, para isso pode ser utilizado o comando: `pip install -r requirements.txt`.

 Após isso, o seguinte comando para iniciar a aplicação: `python3 main.py`.

Existem dois endpoints configurados:

1. `http://localhost:8000/send_file`: método: [POST],

     body exemplo 1: {
    "name" : "Tv",
    "qtd": 1,
    "price" : 2500
    }

     body exemplo 2: {
    "name" : "Tasks",
    "description": ["Task 1", "Task 2", "Task 3"]
    }

    Esse endpoint recebe um json (qualquer formato) como parâmetro, em seguida salva em arquivo os dados da requisição e coloca em uma fila de processamento.

2. `http://localhost:8000/get_next_file` : método: [GET]

    Esse endpoint é responsável por retornar ao usuário o resultado armazenado no próximo arquivo da fila. Os dados são retornados um a um até que a fila fique vazia.

## Dependências

* FastAPI: `main.py`
* json
* datetime 

## Testes

na pasta `tests` existem alguns prints que ilustram a utilização dos endpoints (via postman)
para salvar e ler os arquivos do servidor.