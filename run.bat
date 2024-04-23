@echo off

REM Start the first database container
docker run -p 5672:5672 rabbitmq

REM Wait for a moment before starting the next container
timeout /t 5 /nobreak

REM Start the second database container
docker run -p 5433:5432 database

REM Wait for a moment before starting docker-compose
timeout /t 5 /nobreak

REM Start docker compose
docker-compose up --build
