from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from babies.serializers import BabySerializer

def evaluar_view(user, obj, request):
    return user.username == obj.parent.username

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': evaluar_view,
                    'destroy': evaluar_view,
                    'update': evaluar_view,
                    'partial_update': evaluar_view,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        return Response(serializer.data)
    