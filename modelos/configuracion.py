class Configuracion:
    def __init__(self,
                 membrete_altura=int(32),
                 membrete_pos_x=int(134),
                 membrete_url='',
                 info=[],
                 nota_al_pie=''):
        self._membrete_altura = membrete_altura
        self._membrete_pos_x = membrete_pos_x
        self._membrete_url = membrete_url
        self._info = info
        self._nota_al_pie = nota_al_pie

    def get_membrete_altura(self):
        return self._membrete_altura

    def get_membrete_pos_x(self):
        return self._membrete_pos_x

    def get_membrete_url(self):
        return self._membrete_url

    def get_info(self):
        return self._info

    def get_info_as_string(self):
        cadena=''
        for item in self._info:
            cadena += (item+'\n')
        return cadena.rstrip()

    def get_info_index(self, info=str()):
        return self._info.index(info)

    def get_nota_al_pie(self):
        return self._nota_al_pie

    def set_membrete_altura(self, membrete_altura=int()):
        self._membrete_altura = membrete_altura

    def set_membrete_pos_x(self, membrete_pos_x=int()):
        self._membrete_pos_x = membrete_pos_x

    def set_membrete_url(self, membrete_url=str()):
        self._membrete_url = membrete_url

    def set_info(self, indice=int(), info=str()):
        self._info[indice] = info

    def set_info_as_string(self, info=str()):
        self._info=[]
        for item in info.split('\n'):
            self._info.append(item)

    def add_info(self, info=str()):
        self._info.append(info)

    def pop_info(self, indice=int()):
        if indice < 0 or indice > len(self._info) - 1:
            return False
        return self._info.pop(indice)

    def set_nota_al_pie(self, nota_al_pie=str()):
        self._nota_al_pie = nota_al_pie

    def to_string(self):
        return (str(self._membrete_altura) + '\n' +
                str(self._membrete_pos_x) + '\n' +
                str(self._membrete_url) + '\n' +
                str(self._info) + '\n' +
                str(self._nota_al_pie))

    def convierte_dict_a_configuracion(self, diccionario):
        self.__dict__=diccionario
