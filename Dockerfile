# Imagem base leve com Python 3.11
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Mostra as saídas do print() imediatamente no terminal
ENV PYTHONUNBUFFERED=1

# Copia o código-fonte da aplicação para o container
COPY src/ /app/src/

# Comando executado ao iniciar o container
CMD ["python", "src/main.py"]
