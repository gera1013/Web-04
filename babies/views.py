from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babies.models import Baby
from babies.serializers import BabySerializer

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    
