from django.shortcuts import render
from .models import students
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import studentserializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Create your views here. 


# NOMAL; FUUNCATION BASED
# @api_view(['GET','POST'])
# def Studentcreateandlist(request):
    
#         if request.method ==  'GET':
#             student = students.objects.all()
#             serializer = studentserializer(student,many= True )
#             return Response(serializer.data)
#         elif request.method ==  'POST':
#             serializer  = studentserializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status=status.HTTP_201_CREATED)
#             else:
#                  return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)
            
# @api_view(['GET','DELETE','PUT'])
# def studentedit(request,pk):
#     try:
#         student =   students.objects.get(pk=pk)
#     except student.DoesNotExist:
#          return Response({'error':'Not Found'}, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'GET':
#          serializer=studentserializer(student)
#          return Response(serializer.data)

#     elif request.method =='PUT':
#         serializer = studentserializer(student , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         else:
#              return Response(serializer.error,status = status.HTTP_204_NO_CONTENT)
        
#     elif request.method == 'DELETE':
#         serializer.delete()
#         return Response({'msg':'Deleted'}, status=status.HTTP_200_OK)







class StudentViewSet(ViewSet):
    queryset = students.objects.all()

    def list(self , request):
        queryset = students.objects.all()
        serializer = studentserializer(queryset , many=True)
        return Response(serializer.data)
    
    def retrieve(self , request , pk=None):
        try:
            student = students.objects.get(pk=pk)
        except students.DoesNotExist:
            return Response({'error':'Not Found'}, status = 404)
        
        serializer = studentserializer(student)
        return Response(serializer.data)
    

    def create (self , request):
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def update(self , request , pk=None):
        try:
            student = students.objects.get(pk=pk)
        except student.DoesNotExist:
            return Response({'error':'Not Found'}, status = 404)
        serializer = studentserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=400)
    


    def destroy(self , request , pk=None):
        try:
            student = students.objects.get(pk=pk)
        except student.DoesNotExist:
            return Response({'error':'Not Found'}, status = 404)
        student.delete()
        return Response({'msg':'delete'},status=204)
