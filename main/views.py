from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from main.models import Task
from main.forms import TaskForm

# Create your views here.
def index(request):
      if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                  form.save()
      else:
            form = TaskForm()
      tasks = Task.objects.all()
      return render(request, 'main/index.html', {"todolist": tasks, "form": form})

def delete(request, pk):
      if request.method == 'GET':
            task = get_object_or_404(Task, pk=pk)
            if task:
                  task.delete()
      return HttpResponseRedirect(reverse('index'))

def status(request, pk, value):
      if request.method == 'GET':
            task = get_object_or_404(Task, pk=pk)
            print(task, request.POST)
            if task:
                  if value == 0:
                        task.is_completed = False
                  elif value == 1:
                        task.is_completed = True
                  task.save()
      return HttpResponseRedirect(reverse('index'))