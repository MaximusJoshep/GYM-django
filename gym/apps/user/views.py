from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages	
from django.shortcuts import render, redirect

from .models import User
from django.template import RequestContext

def index(request):
    Users=User.objects.all()
    return render(request, "index_user.html", {"Users": Users })

def register(request):
	return render(request,'add_user.html')

def create(request):
    
	User.objects.create(
		name=request.POST.get('name',False),
		phone=request.POST.get('phone',False),
		address= request.POST.get('address',False),
        username= request.POST.get('username',False),
        password= request.POST.get('password',False),
	)

	return redirect("/users/",  RequestContext(request))
def edit(request, id):
	user= User.objects.get(id=id) 
	return render(request,'add_user.html', {"User": user})


def modify(request, id):
	
	user=User.objects.get(id=id)
	user.name=request.POST.get('name',False)
	user.phone =request.POST.get('phone',False)
	user.address=request.POST.get('address',False)
	user.username = request.POST.get('username',False)
	user.password= request.POST.get('password',False)



	user.save()
	messages.success(request, "Documento editado correctamente")
	return redirect("/users/")
def delete(request, id):
	user=User.objects.get(id=id)
	
	user.delete()
	return redirect("/users/")
def view(request, id):
	user=User.objects.get(id=id)
	return render(request,'view_user.html', {"User": user})
