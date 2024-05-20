# Folosim o imagine de bază Python
FROM python:3.9-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierele de dependențe în container
COPY requirements.txt .

# Instalăm dependențele
RUN pip install -r requirements.txt

# Copiem restul codului în container
COPY . .

# Definim comanda de rulare a aplicației folosind gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
