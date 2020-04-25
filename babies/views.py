from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from babies.serializers import BabySerializer
from parent.models import Parent

def check_baby_is_theirs(user, request):
    _id = (request.POST).get('parent')
    parent = Parent.objects.get(pk=_id)
    return parent.username == user.username

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': check_baby_is_theirs,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': True,
                    'update': 'babies.change_baby',
                    'partial_update': 'babies.change_baby',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)
    