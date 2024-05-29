from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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


class Student_data(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

    def post(self, request, pk=None):
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data has been Saved'}
            return Response(res)
        
        else:
            return Response(serializer.errors)

    def put(self, request, pk=None):
        python_data = request.data
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has been Updated!'}
            return Response(res)
        else:
            return Response(serializer.errors)
        
    def patch(self, request, pk=None):
        python_data = request.data
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has been Updated!'}
            return Response(res)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk=None):
        if id is None:
            return Response({'error': 'ID not provided'})
        stu = Student.objects.get(id=pk)
        stu.delete()
        res = {'msg': 'Data has been deleted'}
        return Response(res)