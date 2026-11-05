class Producto:
    def __init__(self):
        self._automatizado = bool
        self._borrado = bool
        self._producto_url = str()
        self._codigo = str()
        self._tags = list()
        self._nombre = str()
        self._descripcion = str()
        self._costo = float()
        self._ultima_actualizacion_de_costo = str()
        self._tipo_de_cambio = float()
        self._existencias = str()
        self._urlextra = str()
        self._urlextra2 = str()

    def convierte_dict_a_producto(self, diccionario=None):
        if diccionario is None:
            diccionario = dict()
        if diccionario:
            self._automatizado = diccionario['_automatizado']
            self._borrado = diccionario['_borrado']
            self._producto_url = diccionario['_producto_url']
            self._codigo = diccionario['_codigo']
            self._tags = diccionario['_tags']
            self._nombre = diccionario['_nombre']
            self._descripcion = diccionario['_descripcion']
            self._costo = diccionario['_costo']
            self._ultima_actualizacion_de_costo = diccionario['_ultima_actualizacion_de_costo']
            self._tipo_de_cambio = diccionario['_tipo_de_cambio']
            self._existencias = diccionario['_existencias']
            self._urlextra = diccionario['_urlextra']
            self._urlextra2 = diccionario['_urlextra2']

    def get_automatizado (self):
        return self._automatizado

    def get_borrado (self):
        return self._borrado

    def get_producto_url (self):
        return self._producto_url

    def get_codigo (self):
        return self._codigo

    def get_tags (self):
        return self._tags

    def get_nombre (self):
        return self._nombre

    def get_descripcion (self):
        return self._descripcion

    def get_costo (self):
        return self._costo

    def get_ultima_actualizacion_de_costo(self):
        return self._ultima_actualizacion_de_costo

    def get_tipo_de_cambio (self):
        return self._tipo_de_cambio

    def get_existencias (self):
        return self._existencias

    def get_urlextra (self):
        return self._urlextra

    def get_urlextra2 (self):
        return self._urlextra2

    def set_automatizado (self, automatizado=bool):
        self._automatizado = automatizado

    def set_borrado (self, borrado=bool):
        self._borrado = borrado

    def set_producto_url (self, producto_url=str()):
        self._producto_url = producto_url

    def set_codigo (self, codigo=str()):
        self._codigo = codigo

    def add_tag (self, tag=str()):
        self._tags.append(tag)

    def remove_tag (self, tag=str()):
        self._tags.remove(tag)

    def clear_tags (self):
        self._tags.clear()

    def set_nombre (self, nombre=str()):
        self._nombre = nombre

    def set_descripcion (self, descripcion=str()):
        self._descripcion = descripcion

    def set_costo (self, costo=float()):
        self._costo = costo

    def set_ultima_actualizacion_de_costo (self, ultima_actualizacion_de_costo=str()):
        self._ultima_actualizacion_de_costo = ultima_actualizacion_de_costo

    def set_tipo_de_cambio (self, tipo_de_cambio=float()):
        self._tipo_de_cambio = tipo_de_cambio

    def set_existencias (self, existencias=str()):
        self._existencias = existencias

    def set_urlextra (self, urlextra=str()):
        self._urlextra = urlextra

    def set_urlextra2 (self, urlextra2=str()):
        self._urlextra2 = urlextra2

