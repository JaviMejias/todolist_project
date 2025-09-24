from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(
            name="Prueba",
            description="Descripción",
            due_date="2025-08-31"
        )
        self.assertEqual(todo.is_done, False)
        self.assertEqual(todo.name, "Prueba")
        self.assertEqual(str(todo.due_date), "2025-08-31")

    def test_empty_name_should_fail(self):
        todo = Todo(name="", description="Desc", due_date="2025-08-31")
        with self.assertRaises(ValidationError):
            todo.full_clean()

    def test_empty_description_should_fail(self):
        todo = Todo(name="Nombre", description="", due_date="2025-08-31")
        with self.assertRaises(ValidationError):
            todo.full_clean()
