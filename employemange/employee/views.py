from django.shortcuts import render
from .serializers import EmpModelSer
from .models import Employee
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class EmpModelViewSetView(ModelViewSet):
    serializer_class=EmpModelSer
    queryset=Employee.objects.all()
    model=Employee