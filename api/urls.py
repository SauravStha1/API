from django.urls import path
from .views import sample_view, create_student, get_student 

urlpatterns = [
    path('sample/', sample_view, name='sample_view'),
    path('create-student/', create_student),
    path('get-student/', get_student),
]
