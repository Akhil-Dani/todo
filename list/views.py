from django.shortcuts import get_object_or_404, render
from .models import TodoItem
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def todo(request, pk=None):
    if request.method == 'GET':
        if pk:
            todo = get_object_or_404(TodoItem, pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        else:
            todos = TodoItem.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        todo = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        todo = get_object_or_404(TodoItem, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
    


