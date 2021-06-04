<h1>App house</h1>

<h5>Tecnologias utilizadas</h5>

- **Python 3.9.5**
- **Django 3.2**
- **Django Rest Framework**

O App **house** é um projeto backend com o propósito de demonstrar meus conhecimentos em API REST, as definições de uso dos end-points seguem o formato das aplicações padrões desenvolvidas com o Django Rest Framework, ou seja, um end-point trata de uma tabela que é representada por uma model, os verbos utilizados serão os **GET**, **POST**, **PUT** e **DELETE**.

Abaixo seguirá o contrato de como as respostas em _JSON_ serão retornadas e como os _REQUEST_ deverão ser enviadas a aplicação sendo que para os verbos **PUT** e **DELETE** as requisições deverão ser enviadas juntamente o parâmetro ID na URL. Os end-points serão dividos por sua Tabela(Model).

Lembrando que o Django provê uma interface básica para uso/testes dos end-points, que pode ser acessada no endereço no qual a aplicação foi iniciada

**Listar/Criar Imobiliária**

- <https://host:0000/Imobiliaria/>

**Response status**

- **200 OK** - Sucesso
- **201 Created** - Sucesso

**Json**

```json
[
    {
        "nome": "String",
        "endereco": "String"
    }
]
````


**Obter/Excluir/Atualizar Imobiliária**
- <https://host:0000/imobiliaria/{id}>

**Response status**

- **200 OK** - Sucesso

**Parâmetros**

- **ID** -  Id do imobiliaria a ser retornado

**Json**

```json
[
    {
        "nome": "String",
        "endereco": "String"
    }
]
````

**Criar/Listar Imóvel**

- <https://host:0000/Imovel/>

**Response status**

- **200 OK** - Sucesso
- **201 Created** - Sucesso

**Json**

```json
[
    {
        "nome": "String",
        "endereco": "String",
        "descricao": "String",
        "status": 0,
        "caracteristicas": "String",
        "tipo": 0,
        "finalidade": 0,
        "imobiliaria": "00000000-0000-0000-0000-000000000000"
    }
]
````

**Obter/Excluir/Atualizar Imóvel**
- <https://host:0000/Imovel/{id}>

**Response status**

- **200 OK** - Sucesso

**Parâmetros**

- **ID** -  Id do Imóvel a ser retornado

**Json**

```json
[
    {
        "nome": "String",
        "endereco": "String",
        "descricao": "String",
        "status": 0,
        "caracteristicas": "String",
        "tipo": 0,
        "finalidade": 0,
        "imobiliaria": "00000000-0000-0000-0000-000000000000"
    }
]
````
