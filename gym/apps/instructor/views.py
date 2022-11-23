from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages	
from django.shortcuts import render, redirect
from .models import Instructor
from django.template import RequestContext

def index(request):
    Instructores=Instructor.objects.all()
    return render(request, "index_instructor.html", {"Instructores": Instructores })

def register(request):
	return render(request,'add_instructor.html')

def create(request):
    
	Instructor.objects.create(
		instructor_name=request.POST.get('instructor_name',False),
		phone=request.POST.get('phone',False),
		address= request.POST.get('address',False),
		email= request.POST.get('email',False),
	)

	return redirect("/instructors/",  RequestContext(request))
def edit(request, id):
	instructor= Instructor.objects.get(id=id) 
	return render(request,'add_instructor.html', {"Instructor": instructor})


def modify(request, id):
	
	instructor=Instructor.objects.get(id=id)
	instructor.instructor_name=request.POST.get('instructor_name',False)
	instructor.phone =request.POST.get('phone',False)
	instructor.address=request.POST.get('address',False)
	instructor.email=request.POST.get('email',False)


	instructor.save()
	messages.success(request, "Documento editado correctamente")
	return redirect("/instructors/")
def delete(request, id):
	instructor=Instructor.objects.get(id=id)
	
	instructor.delete()
	return redirect("/instructors/")
def view(request, id):
	instructor=Instructor.objects.get(id=id)
	return render(request,'view_instructor.html', {"Instructor": instructor})

