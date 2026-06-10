from django.shortcuts import render
from .models import Note
# from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet

from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import AllowAny

# Create your views here.
# class NoteViewSet(ModelViewSet):
class NoteViewSet(ViewSet.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class =  NoteSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(user=user)

        # filtering
        
        title = self.request.query_params.get('title')
        if title :
            queryset = queryset.filter(title__icontains=title)

        return queryset
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)