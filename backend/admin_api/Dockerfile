# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY main.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer un port si besoin (optionnel)
EXPOSE 8001

# Lancer l'application avec Uvicorn et Unix Socket
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--uds", "/tmp/admin_api.sock"]
