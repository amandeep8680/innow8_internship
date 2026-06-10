from rest_framework import generics ,mixins
from .serializers import aboutprofile
from .models import profiles


class profileshow(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request ):
        return self.list(request )

class profileadd(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def post(self,request, *args, **kwargs):
        return self.create(request ,*args, **kwargs)

class profilesingle(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class profileupdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


class profiledelete(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def perform_destroy(self, instance):
        # 'instance' is the actual object about to be deleted
        print(f"Admin is deleting profile: {instance.name}")
        
        # Actually delete it
        instance.delete()



