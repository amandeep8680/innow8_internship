from rest_framework.permissions  import DjangoModelPermissions
from .models import *
from .serializers import *
from rest_framework import generics
## superadmin - adminn pass 1234



class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [DjangoModelPermissions]