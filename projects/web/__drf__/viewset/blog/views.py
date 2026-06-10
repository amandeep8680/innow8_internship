from rest_framework import viewsets
from .serializers import aboutprofile
from .models import profiles

class profileshow(viewsets.ModelViewSet):
    queryset= profiles.objects.all()
    serializer_class=aboutprofile
