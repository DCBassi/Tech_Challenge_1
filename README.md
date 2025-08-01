# Python Pandas Application

Este projeto é uma aplicação Python que utiliza a biblioteca pandas para carregar e visualizar um dataset, com ambiente pronto para notebooks Jupyter via Docker.

## Estrutura do Projeto

```
TechChallenge
├── src
│   └── 01-exploracao.ipynb
├── diabetes.csv
├── Dockerfile
└── README.md
```

## Requisitos

- Docker instalado na sua máquina.

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/DCBassi/Tech_Challenge_1.git
   cd TechChallenge
   ```

2. Construa a imagem Docker:
   ```
   docker build -t tc-fiap-gaddn .
   ```

## Executando o Jupyter Notebook

Para iniciar o Jupyter Notebook no container, execute:
```
docker run -p 8888:8888 tc-fiap-gaddn
```

Depois, acesse o Jupyter Notebook pelo navegador em [http://localhost:8888](http://localhost:8888) usando o token exibido no terminal.

> **Observação:**  
> O arquivo `diabetes.csv` e a pasta `src` são copiados para o container conforme definido no Dockerfile.  
> O container já inicia o servidor Jupyter Notebook automaticamente.

## Observações

- Não execute arquivos `.ipynb` diretamente com `python`. Use o Jupyter Notebook para abrir e executar os notebooks.
- Certifique-se de que o arquivo `diabetes.csv` está presente na raiz do projeto antes de construir