from rest_framework import viewsets
from guardian.shortcuts import assign_perm
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from parent.models import Parent
from parent.serializers import ParentSerializer

# Función que revisa si el nombre de usuario del usuario actual y el papá es el mismo
def check_is_user(user, request):
    username = (request.POST).get('username')
    return username == user.username

# Viewset para el parent
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


    permission_classes = (
        APIPermissionClassFactory(
            name='ParentPermission',
            permission_configuration={
                'base': {
                    'create': check_is_user,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'parent.view_parent',
                    'destroy': False,
                    'update': 'parent.change_parent',
                    'partial_update': 'babies.change_parent',
                }
            }
        ),
    )

    # Función que brinda los permisos de ver y cambiar papá al usuario que lo crea 
    def perform_create(self, serializer):
        parent = serializer.save()
        user = self.request.user
        assign_perm('babies.view_parent', user, parent)
        assign_perm('babies.change_parent', user, parent)
        return Response(serializer.data)