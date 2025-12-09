from django.urls import path

from .views import StudentView

urlpatterns = [
    # path("sample/", sample_view),
    # path("create-student/", create_student),
    # path("get-students/", get_Student),
    path("students/", StudentView.as_view()),
]