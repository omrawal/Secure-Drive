from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import File
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import api.file_crypto as fc

KEY = b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM='
# Create your views here.


class FileAPIView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request):
        file_data = request.data['file_data']
        encrypted = fc.encrypt(request.data['file_data'].read(), KEY)
        serializer = FileSerializer(
            data={'file_data': str(encrypted), 'file_name': file_data.name, 'file_size': file_data.size, 'file_content_type': file_data.content_type})
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect("http://127.0.0.1:8000/drive/")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response("test")


class FileOperations(APIView):
    def get_file(self, fid):
        try:
            return File.objects.get(fid=fid)
        except File.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, fid):
        file = self.get_file(fid)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def put(self, request, fid):
        file = self.get_file(fid)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fid):
        file = self.get_file(fid)
        file.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# class FiletList(generics.ListCreateAPIView):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer


# class FileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer
#     lookup_field = 'fid'
