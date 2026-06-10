from rest_framework import generics
from .serializers import aboutprofile
from .models import profiles


class profileshow(generics.ListAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

class profileadd(generics.CreateAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

class profilesingle(generics.RetrieveAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

class profileupdate(generics.UpdateAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

class profiledelete(generics.DestroyAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile