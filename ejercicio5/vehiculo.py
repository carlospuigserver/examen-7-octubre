class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas

 

    def __str__(self):

        return "Color {}, {} ruedas".format( self.color, self.ruedas )

    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color

    def set_ruedas(self,ruedas):
        self.ruedas=ruedas
    def get_ruedas(self):
        return self.ruedas



class coche(Vehiculo):
        def __init__(self, color, ruedas, velocidad, cilindrada):
            self.color = color
            self.ruedas = ruedas
            self.velocidad = velocidad
            self.cilindrada = cilindrada

 

        def __str__(self):

           return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )
    
        def set_velocidad(self,velocidad):
            self.velocidad=velocidad
        def get_velocidad(self):
          return self.velocidad
   
        def set_cilindrada(self,cilindrada):
          self.cilindrada=cilindrada
        def get_cilindrada(self):
            return self.cilindrada




class bicicleta(Vehiculo):
     def __init__(self, color, ruedas, tipo):
        super().__innit__(color,ruedas)
        self.tipo=tipo

def __str__(self):

           return "color {}, {} ruedas, {} cc".format( self.color, self.tipo, self.ruedas,)


def set_tipo(self,tipo):
    self.tipo=tipo
def get_tipo(self):
    return self.tipo




class bicicleta(Vehiculo):
     def __init__(self, color, ruedas, tipo):
        super().__innit__(color,ruedas)
        self.tipo=tipo

def __str__(self):

           return "color {}, {} ruedas, {} cc".format( self.color, self.tipo, self.ruedas,)


def set_tipo(self,tipo):
    self.tipo=tipo
def get_tipo(self):
    return self.tipo




class camion(Vehiculo):
     def __init__(self, color, ruedas, carga):
        super().__innit__(color,ruedas)
        self.carga=carga

def __str__(self):

           return "color {}, {} ruedas, {} cc".format( self.color, self.tipo, self.ruedas,)




class motocicleta(Vehiculo):
        def __init__(self, color, ruedas, velocidad, cilindrada):
            super().__innit__(color,ruedas)
            self.velocidad = velocidad
            self.cilindrada = cilindrada

 

        def __str__(self):

           return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )
    
        def set_velocidad(self,velocidad):
            self.velocidad=velocidad
        def get_velocidad(self):
          return self.velocidad
   
        def set_cilindrada(self,cilindrada):
          self.cilindrada=cilindrada
        def get_cilindrada(self):
            return self.cilindrada









 