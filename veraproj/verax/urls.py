from django.urls import path

from .views import StudentList, TestList, TestCreate, StudentCreate

urlpatterns = [
    path('students/', StudentList.as_view(), name="students"),
    path('students/add', StudentCreate.as_view(), name="stu-create"),
    path('tests/', TestList.as_view(), name="tests"),
    path('tests/add', TestCreate.as_view(), name="test-create"),
]