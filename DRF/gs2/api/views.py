from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

# Model object/Instance -- Single Student Data
def StudentDetail(request,pk):
    stu = Student.objects.get(pk=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

# Querry Set -- All Student Data
@api_view(['GET'])
def StudentList(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def Student_data(request,pk=None):
    if request.method == 'GET':
        python_data = request.data
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

    
    elif request.method == 'POST':
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data has been Saved'}
            return Response(res)
        
        else:
            return Response(serializer.errors)

    elif request.method == 'PUT':
        python_data = request.data
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has been Updated!'}
            return Response(res)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PATCH':
        python_data = request.data
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has been Updated!'}
            return Response(res)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        python_data = request.data
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data has been deleted'}
        return Response(res)