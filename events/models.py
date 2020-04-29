from django.db import models

# Clase model para eventos.
# Campos: descripción, tipo, fecha y bebé
class Event(models.Model):
    description = models.CharField(max_length = 500)
    event_type = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add=True)
    baby = models.ForeignKey(
        'babies.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    def __str__(self):
        return '{}'.format(self.description)
