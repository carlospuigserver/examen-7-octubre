class Alumno:
    def __init__(self, nombre, nota):
      self.nombre = nombre
      self.nota = nota
      print("El alumno ha sido creado con éxito")
    
    def notas(self):
        if self.nota<5:
            print("{} el alumno ha suspendido".format(self.alumno))
        else:
            print("{} el alumno ha aprobado".format(self.alumno))


