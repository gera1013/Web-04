from django.db import models

# Clase model para papás.
# Campos: nombre y nombre de usuario
class Parent(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)

    def __str__(self):
        return '{}'.format(self.name)