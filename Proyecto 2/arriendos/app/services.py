from .models import Inmueble, Tipo_inmueble, User

def get_all_inmuebles():
    # Utilizamos el ORM de Django para obtener todos los inmuebles
    inmueble = Inmueble.objects.all()
    return inmueble


def insertar_inmueble(nombre_inmueble, m2_construido, numero_banos, numero_hab, direccion):
    # Creamos un nuevo objeto Inmueble con los datos proporcionados
    nuevo_inmueble = Inmueble(nombre_inmueble=nombre_inmueble, 
                              m2_construido=m2_construido,
                              numero_banos=numero_banos,
                              numero_hab=numero_hab,
                              direccion=direccion)
    # Guardamos el nuevo inmueble en la base de datos
    nuevo_inmueble.save()


def actualizar_inmueble(id_inmueble, nombre_inmueble, m2_construido, numero_banos, numero_hab, direccion):
    # Obtenemos el inmueble que queremos actualizar
    inmueble = Inmueble.objects.get(id=id_inmueble)
    # Actualizamos sus atributos
    inmueble.nombre_inmueble = nombre_inmueble
    inmueble.m2_construido = m2_construido
    inmueble.numero_banos = numero_banos
    inmueble.numero_hab = numero_hab
    inmueble.direccion = direccion
    # Guardamos los cambios en la base de datos
    inmueble.save()


def borrar_inmueble(id_inmueble):
    # Obtenemos el inmueble que queremos borrar
    inmueble = Inmueble.objects.get(id=id_inmueble)
    # Borramos el inmueble de la base de datos
    inmueble.delete()
