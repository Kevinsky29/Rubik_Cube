from ursina import *
from itertools import product

app = Ursina()

# Agregar una entidad para mostrar los controles
controls_text = Text(text='Controles:\nU,u: Mover capa superior \nD,d: Mover capa inferior\nL,l: Mover capa izquierda \nR,r: Mover capa derecha\nF,f: Mover capa frontal\nB,b: Mover capa trasera', 
                     position=(-0.7, 0.3), scale=1, background=False)

# Función para agrupar los cubos por capa
def relacion_padre_hijo(eje, capa):
  
  for cubo in cubos:
    cubo.position, cubo.rotation = round(cubo.world_position, 1), cubo.world_rotation
    cubo.parent = scene  # Todos los cubos pertenecen a la escena
  
  centro.rotation = 0  # Se reinicia la rotación del centro
  
  # Se agrupan los cubos por capa
  for cubo in cubos:
    if eval(f'cubo.position.{eje}') == capa:
      cubo.parent = centro


# Función para detectar los movimientos de los controles
def input(key):
  if key not in rot_dict: return  # Se verifica si la tecla presionada es válida
  eje, capa, angulo = rot_dict[key]
  relacion_padre_hijo(eje, capa)
  shift = held_keys['shift']
  eval(f'centro.animate_rotation_{eje} ({-angulo if shift else angulo}, duration = 0.5)')  # Se realiza la rotación del centro en el eje correspondiente

window.borderless = False
window.fullscreen = True
EditorCamera()

centro = Entity()  # Entidad para agrupar los cubos del centro

# Diccionario que contiene información sobre los movimientos que se pueden hacer
# Las llaves son las teclas de movimiento, y los valores son una lista con tres elementos:
# el eje de rotación (x, y, o z), la capa de rotación (1, -1), y el ángulo de rotación (en grados)
rot_dict = {'u': ['y', 1, 90],  'd': ['y', -1, -90],
            'l': ['x', -1, -90], 'r': ['x', 1, 90],
            'f': ['z', -1, 90],  'b': ['z', 1, -90]}


cubos = []
for pos in product((-1,0,1), repeat=3):
  cubos.append(Entity(model='/models/Teil_46_model.obj', texture = '/textures/rubik_texture.png', position=pos, scale=0.5))  # Se crean los cubos

app.run()  # Se ejecuta la aplicación
