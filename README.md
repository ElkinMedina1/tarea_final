# 🪗 Sistema de Gestión de Obras Musicales: Folklore Vallenato

Este proyecto es una implementación avanzada de **Programación Orientada a Objetos (POO)** en Python. Utiliza la analogía de un conjunto vallenato para demostrar conceptos críticos de ingeniería de software requeridos en la asignatura de Programación.

## 🎯 Objetivos del Proyecto
Desarrollar un sistema robusto que integre:
1.  **Abstracción** mediante el módulo `abc`.
2.  **Herencia Múltiple** para la composición de funcionalidades.
3.  **Encapsulamiento** con validación lógica de datos.
4.  **Polimorfismo** en la ejecución de métodos heredados.

---

## 🏗️ Arquitectura del Software

El sistema se divide en tres capas de clases:

### 1. Clase Base Abstracta (`obra_musical`)
Define el contrato esencial. Ninguna obra puede existir sin un **título**, una **voz líder** y un **compositor**. Obliga a las clases hijas a implementar:
* `interpretar()`: La lógica de ejecución de la pieza.
* `__str__()`: La representación formal de la ficha técnica.

### 2. Módulos de Apoyo (Mixins)
* **`acordeon`**: Gestiona la marca y el modelo del instrumento, aportando el método `tocar()`.
* **`base_ritmo`**: Define el aire vallenato (Paseo, Merengue, Son, Puya) y aporta el método `marcar_ritmo()`.

### 3. Clase Final (`cancion_vallenata`)
Es el núcleo del sistema. Hereda de las tres clases anteriores y aplica **Encapsulamiento Robusto**:
* El atributo `_duracion` es privado.
* Se accede mediante `@property` (Getter).
* Se modifica mediante un `@setter` que valida que la canción dure al menos **60 segundos**, evitando datos incoherentes en el sistema.

---

## 💻 Ejemplo de Uso

```python
# Instanciación de un objeto
cancion = cancion_vallenata("La Plata", "Diomedes Díaz", "Calixto Ochoa", "Paseo", 245)

# Ejecución de polimorfismo
print(cancion)
cancion.interpretar()

# Prueba de protección de datos
cancion.duracion = 20  # Esto disparará un error de validación
