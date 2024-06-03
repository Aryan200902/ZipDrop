from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer

def home(request):
    return render(request,'home.html')

def download(request, uid):
    return render(request, 'download.html',context = {'uid': uid})

class HandleFileUpload(APIView):
    def post(self, request):
        serializer = FileListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Files Uploaded Successfully',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 400,
                'message': 'Something Went Wrong',
                'data': serializer.errors
            })
