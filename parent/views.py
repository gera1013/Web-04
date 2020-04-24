from rest_framework import viewsets

from parent.models import Parent
from parent.serializers import ParentSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
