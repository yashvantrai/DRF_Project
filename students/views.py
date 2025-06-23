from django.shortcuts import render
from django.http import HttpResponse

def students(reuest):
    students = [
        {'id': 1, 'name':'john doe', 'age': 25}
    ]
    return HttpResponse(students)
