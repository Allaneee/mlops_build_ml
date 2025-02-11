import os
import uvicorn
from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Charger les variables d'environnement
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
SOCKET_FILE = os.getenv("USER_API_SOCKET")

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

@app.get("/")
def read_root():
    return {"message": "User API is running"}

@app.post("/users/")
def create_user(name: str, email: str):
    """Ajoute un utilisateur à la base de données."""
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    return {"id": user_id, "name": name, "email": email}

if __name__ == "__main__":
    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)
    uvicorn.run(app, uds=SOCKET_FILE)
