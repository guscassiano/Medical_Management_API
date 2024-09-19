# Projeto API de Consultas Médicas

Este projeto é uma API para gerenciar pacientes e consultas médicas, desenvolvida com Django e Django Rest Framework (DRF). A API oferece funcionalidades de criação, leitura, atualização e exclusão (CRUD) de pacientes e consultas, possibilidade de realização de filtros utilizados com Django RQL, além de autenticação via JWT para usuários da API e paginação para facilitar o consumo dos dados.

## Funcionalidades

- Gerenciamento de Pacientes: cadastro, visualização, edição e exclusão.
- Gerenciamento de Consultas: criação, visualização, edição e exclusão de consultas associadas a pacientes.
- Autenticação via JWT.
- Paginação nos endpoints de listagem.
- Filtragem dos dados com Django RQL.

## Tecnologias Utilizadas

- Django
- Django Rest Framework (DRF)
- Django RQL (Resource query language)
- JWT (JSON Web Tokens)
- SQLite (banco de dados padrão)

## Requisitos

Certifique-se de ter o Python 3.12 instalado. As dependências do projeto estão listadas no arquivo `requirements.txt`.

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/guscassiano/Medical_Management_API.git
cd Medical_Management_API
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o Django Admin e outros usuários, além de gerenciar todos cadastros da API:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Autenticação JWT

A API utiliza JWT para autenticação. Após realizar o login, um token de acesso será gerado. Para acessar endpoints protegidos, envie o token no cabeçalho da requisição:

Authorization: Bearer <seu-token-jwt>

### Gerando Token

Você pode obter um token enviando uma requisição POST para /api/token/ com as credenciais do usuário:

```json
{
    "username": "seu-usuario",
    "password": "sua-senha"
}
```

Isso retornará um token JWT que poderá ser usado para autenticar as requisições subsequentes.

## Testes

O projeto inclui testes unitários para garantir o correto funcionamento da API. Para rodar os testes, use o comando:

```bash
python manage.py test
```

## Paginação

Os endpoints de listagem estão paginados por padrão, com um limite de 10 itens por página. Para navegar entre as páginas, utilize os parâmetros ```bash?page=``` na URL.

## Filtros RQL

A biblioteca Django RQL fornece diversos filtros para as URLS de APIs.
Na documentação pode ser verificado todos os filtros possíveis:
    [link](https://django-rql.readthedocs.io/en/latest/user_guide/)

Segue exemplo abaixo de um filtro realizado na API de consultas através do ID do paciente:

[link](http://127.0.0.1:8000/api/v1/consultation/?eq(patient_name,3))

Este exemplo retorna somente as informações do paciente 3.

## Contribuições

Sinta-se à vontade para enviar pull requests ou abrir issues para sugerir melhorias.
