## Introduction

Ce projet met en place une architecture MLOps avec des microservices en FastAPI, une base de données PostgreSQL, et un reverse proxy Nginx pour centraliser les requêtes.
Les APIs utilisent Unix Sockets pour une communication optimisée.

## Composants principaux

PostgreSQL → Stocke les données des utilisateurs et des logs d’administration.
User API (FastAPI) → Gère les utilisateurs et communique avec la base de données.
Admin API (FastAPI) → Gère les logs et l’administration.
Nginx → Reverse proxy qui redirige les requêtes vers les bonnes APIs.
Docker Compose → Orchestre le déploiement des services.

## Schéma:

Utilisateur → Nginx → (User API | Admin API) → PostgreSQL

## Démarrage: 

docker-compose up --build -d
