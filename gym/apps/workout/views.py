from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages	
from django.shortcuts import render, redirect
from .models import Workout
from django.template import RequestContext

from .models import Workout, WorkoutPlan


def index(request):
    Workouts=Workout.objects.all()
    return render(request, "index_workout.html", {"Workouts": Workouts })

def register(request):
	return render(request,'add_workout.html')

def create(request):
    
	Workout.objects.create(
		workout_name=request.POST.get('workout_name',False),
		description=request.POST.get('description',False),
	
	)

	return redirect("/workouts/",  RequestContext(request))
def edit(request, id):
	workout= Workout.objects.get(id=id) 
	return render(request,'add_workout.html', {"Workout": workout})


def modify(request, id):
	
	workout=Workout.objects.get(id=id)
	workout.workout_name=request.POST.get('workout_name',False)
	workout.phone =request.POST.get('description',False)



	workout.save()
	messages.success(request, "Documento editado correctamente")
	return redirect("/workouts/")
def delete(request, id):
	workout=Workout.objects.get(id=id)
	
	workout.delete()
	return redirect("/workouts/")
def view(request, id):
	workout=Workout.objects.get(id=id)
	return render(request,'view_workout.html', {"Workout": workout})
