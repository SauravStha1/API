from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CreateStudentSerializer, ShowStudentSerializer
from .models import student

@api_view(['GET'])
def sample_view(request):
    data = {'message': 'Hello, this is a sample API response!',
            "name": 'Saurav',}
    return Response(data)   

@api_view(['GET'])
def get_student(request):
    students = student.objects.all()
    serializer = ShowStudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = CreateStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)