from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(nombre):
    curso = Curso.objects.create(nombre=nombre)
    return curso

def crear_profesor(nombre, direccion):
    direccion_obj = Direccion.objects.create(**direccion)
    profesor = Profesor.objects.create(nombre=nombre, direccion=direccion_obj)
    return profesor

def crear_estudiante(nombre, direccion):
    direccion_obj = Direccion.objects.create(**direccion)
    estudiante = Estudiante.objects.create(nombre=nombre, direccion=direccion_obj)
    return estudiante

def crear_direccion(calle, ciudad, pais):
    direccion = Direccion.objects.create(calle=calle, ciudad=ciudad, pais=pais)
    return direccion

def obtiene_estudiante(estudiante_id):
    return Estudiante.objects.get(id=estudiante_id)

def obtiene_profesor(profesor_id):
    return Profesor.objects.get(id=profesor_id)

def obtiene_curso(curso_id):
    return Curso.objects.get(id=curso_id)

def agrega_profesor_a_curso(profesor_id, curso_id):
    profesor = Profesor.objects.get(id=profesor_id)
    curso = Curso.objects.get(id=curso_id)
    curso.profesores.add(profesor)
    return curso

def agrega_cursos_a_estudiante(estudiante_id, cursos_ids):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    for curso_id in cursos_ids:
        curso = Curso.objects.get(id=curso_id)
        estudiante.cursos.add(curso)
    return estudiante

def imprime_estudiante_cursos(estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    cursos = estudiante.cursos.all()
    cursos_nombres = [curso.nombre for curso in cursos]
    return cursos_nombres
