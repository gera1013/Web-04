from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.response import Response

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
                    'update': 'events.change_event',
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.view_event', user, event)
        assign_perm('events.change_event', user, event)
        return Response(serializer.data)