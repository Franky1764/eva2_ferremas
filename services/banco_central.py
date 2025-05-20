import requests
from datetime import date

# Cargar credenciales desde archivo de texto (una línea con user, otra con pass)
with open("credenciales.txt", "r") as f:
    user = f.readline().strip()
    password = f.readline().strip()

# Código oficial del tipo de cambio observado diario USD/CLP
SERIE_ID = "F073.TCO.PRE.Z.D"

def obtener_dolar_actual():
    try:
        hoy = date.today().strftime("%Y-%m-%d")
        url = (
            f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?"
            f"user={user}&pass={password}&function=GetSeries"
            f"&timeseries={SERIE_ID}&firstdate={hoy}&lastdate={hoy}"
        )

        response = requests.get(url)
        data = response.json()

        # Extraer último valor
        obs = data.get("Series", {}).get("Obs", [])
        if obs:
            valor = float(obs[-1]["value"].replace(",", "."))
            return valor

        print("No hay observaciones disponibles")
        return None

    except Exception as e:
        print(f"ERROR al consultar el dólar: {e}")
        return None



