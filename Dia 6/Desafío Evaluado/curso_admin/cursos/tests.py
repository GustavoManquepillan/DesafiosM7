from django.test import TestCase
from .services import *
from .models import Direccion, Profesor, Estudiante, Curso

class ServiciosTest(TestCase):
    def setUp(self):
        self.direccion = {'calle': '123 Calle', 'ciudad': 'Ciudad', 'pais': 'Pais'}
        self.profesor = crear_profesor('Profesor 1', self.direccion)
        self.curso = crear_curso('Curso 1')
        self.estudiante = crear_estudiante('Estudiante 1', self.direccion)

    def test_crear_curso(self):
        curso = crear_curso('Curso 2')
        self.assertEqual(curso.nombre, 'Curso 2')

    def test_crear_profesor(self):
        profesor = crear_profesor('Profesor 2', self.direccion)
        self.assertEqual(profesor.nombre, 'Profesor 2')

    def test_crear_estudiante(self):
        estudiante = crear_estudiante('Estudiante 2', self.direccion)
        self.assertEqual(estudiante.nombre, 'Estudiante 2')

    def test_agregar_profesor_a_curso(self):
        curso = agrega_profesor_a_curso(self.profesor.id, self.curso.id)
        self.assertIn(self.profesor, curso.profesores.all())

    def test_agregar_cursos_a_estudiante(self):
        cursos_ids = [self.curso.id]
        estudiante = agrega_cursos_a_estudiante(self.estudiante.id, cursos_ids)
        self.assertIn(self.curso, estudiante.cursos.all())

    def test_imprime_estudiante_cursos(self):
        cursos_ids = [self.curso.id]
        estudiante = agrega_cursos_a_estudiante(self.estudiante.id, cursos_ids)
        cursos_nombres = imprime_estudiante_cursos(self.estudiante.id)
        self.assertIn('Curso 1', cursos_nombres)