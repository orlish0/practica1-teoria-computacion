ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# Entorno virtual en /opt/venv fuera de /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Capa de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Flet en modo servidor web para contenedor
ENV FLET_FORCE_WEB_SERVER=true
ENV FLET_SERVER_PORT=8550

CMD ["python", "src/app.py"]
