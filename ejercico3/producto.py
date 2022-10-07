class Producto:
 
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
 
    def __str__(self):
        return """\
CODIGO\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
TIPO\t{}""".format(self.codigo, self.nombre, self.precio, self.tipo)
@property
 
def codigo(self):
 
    return self.__codigo
 
@codigo.setter
 
def codigo(self, nuevoValor):
 
    self.__codigo = nuevoValor
 
@property
 
def nombre(self):
 
    return self.__nombre
 
@nombre.setter
 
def nombre(self, nuevoValor):
 
    self.__nombre = nuevoValor
 
@property
 
def precio(self):
 
    return self.__precio
 
@precio.setter
 
def precio(self, nuevoValor):
 
    self.__precio = nuevoValor
 
@property
 
def tipo(self):
 
    return self.__tipo
 
@tipo.setter
 
def tipo(self, nuevoValor):
 
    self.__tipo = nuevoValor