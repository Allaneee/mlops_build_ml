# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY main.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer un port si besoin (optionnel, car on utilise Unix Sockets)
EXPOSE 8000

# Lancer l'application avec Uvicorn et Unix Socket
CMD ["python", "main.py"]
