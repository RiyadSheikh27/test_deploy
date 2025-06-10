from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def car_management(request):
    return render(request, 'cars/car_management.html')

class CarsViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(models.Cars, id=id)
            serializer = serializers.CarsSerializer(item)
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)

        items = models.Cars.objects.all()
        serializer = serializers.CarsSerializer(items, many=True)
        return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = get_object_or_404(models.Cars, id=id)
        serializer = serializers.CarsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(models.Cars, id=id)
        item.delete()
        return Response({"status":"success","data":"Item Deleted"})