from django.db import models

# Clase model para eventos.
# Campos: nombre, apellido, edad y papá (foreign key al modelo parent)
class Baby(models.Model):
    name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(
        'parent.Parent',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    def __str__(self):
        return '{}'.format(self.name)