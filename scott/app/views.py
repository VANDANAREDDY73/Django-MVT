from django.shortcuts import render
from app.models import *
# Create your views here.
def dept(request):
  QLDO=Dept.objects.all()
  d={'Depts':QLDO}
  return render(request,'dept.html',d)

def emp(request):
  QLEO=Emp.objects.all()
  d={'Emps':QLEO}
  return render(request,'emp.html',d)