from django.urls import path

from .views import StudentList, TestList, TestCreate

urlpatterns = [
    path('students/', StudentList.as_view(), name="students"),
    path('tests/', TestList.as_view(), name="tests"),
    path('tests/add', TestCreate.as_view(), name="create"),
]