from guardian.shortcuts import assign_perm
from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from events.models import Event
from events.serializers import EventSerializer

def evaluar(user, obj, request):
    return user.username == obj.baby.parent.username

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': evaluar,
                    'destroy': evaluar,
                    'update': evaluar,
                    'partial_update': evaluar,
                }
            }
        ),
    )