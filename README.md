# base-system-flask

## Em construção

## Como iniciar o projeto

### Pré-requisitos

- Python 3.8+
- Docker e Docker Compose (opcional)
- pip

### Instalação local

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/base-system-flask.git
   cd base-system-flask
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor Flask:
   ```bash
   python routes.py
   ```

5. Acesse a documentação Swagger:
   ```
   http://localhost:8000/apidocs/
   ```

### Usando Docker

1. Suba os containers:
   ```bash
   docker-compose up
   ```

2. Acesse a API e a documentação Swagger normalmente:
   ```
   http://localhost:8000/apidocs/
   ```

## Observações

- Para autenticação JWT, faça login na rota `/login` e use o token retornado no botão "Authorize" do Swagger, sempre com o prefixo `Bearer `.
- As variáveis de ambiente podem ser configuradas em um arquivo `.env` se necessário.

### Comandos

`docker-compose up`
