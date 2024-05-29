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
def Student_data(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data has been Saved'}
            json_data = json.dumps(res)
            return HttpResponse(json_data, content_type='application/json')
        
        else:
            json_data = json.dumps(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has been Updated!'}
            return JsonResponse(res,safe=False)
            # json_data = json.dumps(res)
            # return HttpResponse(json_data, content_type='application/json')
        else:
            return JsonResponse(serializer.errors, safe=False)
            # json_data = json.dumps(serializer.errors)
            # return HttpResponse(json_data, content_type='application/json')
        
    elif request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data has been deleted'}
        json_data = json.dumps(res)
        return HttpResponse(json_data, content_type='application/json')