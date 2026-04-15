from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import aboutprofile
from .models import profiles

class abouts(APIView):
    # Add pk=None here to prevent the error
    def get(self, request, pk=None):
        if pk:
            # If an ID is provided, get that single profile
            try:
                person = profiles.objects.get(pk=pk)
                serializer = aboutprofile(person)
                return Response(serializer.data)
            except profiles.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # If no ID, get all profiles (list view)
        person = profiles.objects.all()
        serializer = aboutprofile(person, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Post usually doesn't need PK
        serializer = aboutprofile(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            # FIX: changed .object to .objects
            person = profiles.objects.get(pk=pk) 
        except profiles.DoesNotExist:
            return Response({"error": "No profile found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = aboutprofile(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) # FIX: Use 200 OK
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            person = profiles.objects.get(pk=pk) # FIX: changed .object to .objects
            person.delete()
            return Response({"message": "Profile deleted"}, status=status.HTTP_200_OK)
        except profiles.DoesNotExist:
            return Response({"error": "No profile found"}, status=status.HTTP_404_NOT_FOUND)