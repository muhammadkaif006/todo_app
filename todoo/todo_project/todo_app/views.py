from django.shortcuts import render, redirect
from .models import tasks
from .forms import model
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class taskListView(ListView):
    model = tasks
    template_name = 'index.html'
    context_object_name = 'tasks'

class detailview(DetailView):
    model = tasks
    template_name = 'detail.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = tasks
    template_name = 'edit.html'
    context_object_name = 'tasks'
    fields = ('heading', 'description', 'date', 'time')
    success_url = reverse_lazy('todo_app:funtask')

class deleteview(DeleteView):
    model = tasks
    success_url = reverse_lazy('todo_app:funtask')

def funtask(request):
    todo = tasks.objects.all()
    return render(request, 'index.html', {'tasks': todo})

def addtask(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        t = tasks(heading=heading, description=description, date=date, time=time)
        t.save()
        return redirect('/')
    else:
        return render(request, 'addtask.html')

def delete(request, id):
    task = tasks.objects.get(id=id)
    task.delete()
    return redirect('/')
def update(request, id):
    task = tasks.objects.get(id=id)
    form = model(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})
