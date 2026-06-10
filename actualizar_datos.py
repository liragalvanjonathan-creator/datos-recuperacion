import requests
import pandas as pd

# Configuración de tu sistema
PROJECT_ID = "marr-5c38a"
API_KEY = "AIzaSyBNx4SVs0PBYzTH6VKeC2Rt2or-jPNXShE"

def fetch_collection(name):
    url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default )/documents/{name}?key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200: return []
    docs = response.json().get('documents', [])
    data = []
    for doc in docs:
        fields = doc.get('fields', {})
        row = {k: list(v.values())[0] for k, v in fields.items()}
        data.append(row)
    return data

# Bajamos los datos y los guardamos
datos = fetch_collection("production")
df = pd.DataFrame(datos)
df.to_csv("datos_operadores.csv", index=False)
print("Archivo generado con éxito")
