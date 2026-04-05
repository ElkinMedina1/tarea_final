from abc import ABC, abstractmethod
class obra_musical(ABC):
    def __init__(self,titulo,voz_lider,compositor):
        self.titulo=titulo
        self.voz_lider=voz_lider
        self.compositor=compositor

    @abstractmethod
    def interpretar(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

class acordeon():
    def __init__(self,marca="Honher",modelo="III"):
        self.marca=marca
        self.modelo=modelo
    
    def tocar(self):
            print("Tocando el acordeon")
        
class base_ritmo ():
    def __init__(self,ritmo="paseo"):
        self.ritmo=ritmo
    
    def marcar_ritmo(self):
        print(f"Marcando el ritmo de {self.ritmo}")

class cancion_vallenata (obra_musical,acordeon,base_ritmo):
    def __init__(self, titulo, voz_lider, compositor,ritmo,duracion_seg):
        obra_musical.__init__(self,titulo,voz_lider,compositor)
        acordeon.__init__(self)
        base_ritmo.__init__(self,ritmo)
        
        self._duracion=None
        self.duracion=duracion_seg
    def interpretar(self):
        print(f"interpretando la cancion '{self.titulo}' con voz líder de {self.voz_lider} y compositor {self.compositor}.")
        self.tocar()
        self.marcar_ritmo()
        print(f"Duración: {self.duracion} segundos.")
    def __str__(self):
        return f"Vallenato: {self.titulo} ({self.ritmo}) - {self.voz_lider}"
    
    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self, valor):
        if not isinstance(valor, int) or valor < 60:
            print(f" error: La duración de '{self.titulo}' debe ser mayor a 60 segundos.")
        else: 
            self._duracion = valor
            print(f"la duracion asigmnada es :{self._duracion} segundos")
 
if __name__ == "__main__":
    cancion1 = cancion_vallenata("La Plata", "Diomedes Díaz", "Calixto Ochoa", "Paseo", 245)
    cancion2 = cancion_vallenata("El Cantor de Fonseca", "Jorge Oñate", "Huaco Almenárez", "Merengue", 310)
    cancion3 = cancion_vallenata("La Juntera", "Diomedes Díaz", "Marciano Martínez", "Paseo", 215)
    
    print("\n DEMOSTRACIÓN DE POLIMORFISMO Y MÉTODOS HEREDADOS ---")
    repertorio = [cancion1, cancion2, cancion3]
    
    for cancion in repertorio:
        print(f"\n info: {cancion}")
        print(cancion.interpretar())
    
    print("\n prueba dee validacion ")
    print(f"lectura de la cancion 1 {cancion1.titulo}): {cancion1.duracion} segundos.")
    print("\n vamos a actualizar la duracion a 300 segundos...")
    cancion1.duracion = 300 
    print(f" el nuevo cambio es de: {cancion1.duracion} segundos.")
    print("\n vamos a actualizar la  duracion a 20 segundos...")
    cancion1.duracion = 20
    print(f"Lectura tras intento fallido: {cancion1.duracion} segundos.")

    




