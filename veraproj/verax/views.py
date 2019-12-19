from django.shortcuts import render
from django.urls import reverse

from .models import Student, Test
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# Create your views here.

class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = "studentlist.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context

class TestList(ListView):
    model = Test
    context_object_name = 'tests';
    template_name = "testlist.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context

class TestCreate(CreateView):
    model = Test
    fields = ['name', 'student', 'grade']
    template_name = "test_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('students')

class StudentCreate(CreateView):
    model = Student
    fields = ['name']
    template_name = "student_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('students')