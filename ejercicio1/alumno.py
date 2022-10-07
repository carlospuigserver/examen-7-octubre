class Alumno:
    def __init__(self, nombre, nota):
      self.nombre = nombre
      self.nota = nota
      print("El alumno ha sido creado con éxito")
    
    def notas(self):
        if self.nota<5:
            print("{} el alumno ha suspendido".format(self.alumno))
            return "suspenso"
        else:
            print("{} el alumno ha aprobado".format(self.alumno))
            return "aprobado"


    def __str__(self):
        return f"({self.nombre} ({self.notas})"

    
    