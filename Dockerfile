FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY .env.example .env

# O Cloud Run espera que o container responda a requisições HTTP por padrão.
# Se for rodar via Scheduler como um job, a imagem precisa rodar o script e sair com sucesso.
CMD ["python", "src/main.py"]
