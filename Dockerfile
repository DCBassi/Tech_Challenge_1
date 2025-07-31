# Usa uma imagem base Python oficial que já inclui algumas ferramentas
FROM jupyter/scipy-notebook:latest

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dados (se houver) para o diretório de trabalho
COPY diabetes.csv .

# Copia toda a pasta 'src' para o diretório de trabalho do container
COPY src/ ./src/

# Comando para iniciar o Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]