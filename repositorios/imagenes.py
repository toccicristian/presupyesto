import io
from urllib.request import urlopen


def obtiene_de_url(url=str()):
    try:
        pagina = urlopen(url)
        imagen = io.BytesIO(pagina.read())
        return imagen
    except:
        return False

