from flask import Flask, Response
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Contador de solicitudes
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Cantidad total de solicitudes recibidas"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    logging.info("Solicitud recibida en la ruta principal.")
    return "Microservicio DevOps funcionando"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    logging.info("Iniciando Microservicio DevOps...")
    app.run(host="0.0.0.0", port=5000)
