from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from events.models import Event
from events.serializers import EventSerializer
from babies.models import Baby

# Función que revisa si el evento está siendo creado para un bebé
# perteneciente al usuario
def check_baby_is_theirs(user, request):
    _id = (request.POST).get('baby')
    baby = Baby.objects.get(pk=_id)
    return baby.parent.username == user.username


# Se define viewset de eventos
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # Permisos para el CRUD de eventos
    # Revisa que el usuario que desea hacer las modificaciones cuenta
    # con los permisos necesarios
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': check_baby_is_theirs,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': True,
                    'update': 'events.change_event',
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    # Brinda permisos de ver y cambiar evento al usuario que ha creado el evento
    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.view_event', user, event)
        assign_perm('events.change_event', user, event)
        assign_perm('events.delete_event', user, event)
        return Response(serializer.data)