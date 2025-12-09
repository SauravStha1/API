from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from .serializers import CreateStudentSerializer, ShowStudentSerializer

#  Create your views here.
from .models import student


@api_view(["GET"])
def sample_view(request):
    data = {
        "message": "This is a sample API response",
        "status": "success",
        "status_code": 200,
        "data": {
            "name": "kushal",
            "age": 24,
            "city": "pokhara",
        },
    }
    return Response(data)


@api_view(["GET"])
def get_Student(request):
    students = student.objects.all()
    serializer = ShowStudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_student(request):
    if request.method == "POST":
        serializer = CreateStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "Student created successfully"}
            return Response(serializer.data, status=201, headers=message)
        return Response(serializer.errors, status=400)



class StudentView(APIView):
    # get method
    def get(self, request):
        students = student.objects.all()
        serializer = ShowStudentSerializer(students, many=True)
        return Response(serializer.data)
###
    def post(self, request):
        serializer = CreateStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "Student created successfully"}
            return Response(serializer.data, status=201, headers=message)
        return Response(serializer.errors, status=400)