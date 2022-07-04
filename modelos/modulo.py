import os


class Modulo:
    def __init__(self, url=str()):
        self._url = os.path.expanduser(os.path.normpath(url))

    def get_url(self):
        return self._url

    def get_paquete(self):
        return os.path.split(self._url)[0].lstrip('./').replace('/', '.').rstrip(',')

    def get_modulo(self):
        return os.path.split(self._url)[1].rstrip('.py')

    def get_importable(self):
        return os.path.split(self._url)[0].lstrip('./').replace('/', '.').rstrip(',') + '.' + os.path.split(self._url)[
            1].rstrip('.py')
